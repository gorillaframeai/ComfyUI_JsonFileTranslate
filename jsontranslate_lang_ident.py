import json
import re
import argparse
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from deep_translator import GoogleTranslator

def is_chinese(text):
    # Проверяем, содержит ли текст китайские символы
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')
    return bool(chinese_pattern.search(text))

def translate_text(text, source_lang, target_lang):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_text = translator.translate(text)
    print(f"Переведено: {text} -> {translated_text}")
    return translated_text

def translate_texts(texts, source_lang, target_lang, max_workers=10):
    translated_texts = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_text = {executor.submit(translate_text, text, source_lang, target_lang): text for text in texts}
        for future in as_completed(future_to_text):
            translated_text = future.result()
            translated_texts.append(translated_text)
    return translated_texts

def process_json(json_data, source_lang, target_lang, max_workers=10):
    # Список для хранения путей к строкам, которые нужно перевести
    paths_to_translate = []

    def recursive_collect(data, path):
        if isinstance(data, dict):
            for key, value in data.items():
                recursive_collect(value, path + [key])
        elif isinstance(data, list):
            for index, item in enumerate(data):
                recursive_collect(item, path + [index])
        elif isinstance(data, str):
            if is_chinese(data):
                paths_to_translate.append((path, data))  # Сохраняем путь и строку
        # Другие типы данных (числа, булевы значения и т.д.) не обрабатываем

    # Собираем все строки, которые нужно перевести, и их пути
    print("Сбор строк для перевода...")
    recursive_collect(json_data, [])
    print(f"Собрано {len(paths_to_translate)} строк для перевода.")

    # Переводим все строки параллельно
    if paths_to_translate:
        print("Начало перевода...")
        texts_to_translate = [text for _, text in paths_to_translate]
        translated_texts = translate_texts(texts_to_translate, source_lang, target_lang, max_workers)
        print("Перевод завершен.")

        # Проверка соответствия количества переведенных строк количеству собранных строк
        if len(translated_texts) != len(paths_to_translate):
            raise ValueError(f"Количество переведенных строк ({len(translated_texts)}) не соответствует количеству собранных строк ({len(paths_to_translate)})")

        # Заменяем строки в JSON на переведенные
        for (path, _), translated_text in zip(paths_to_translate, translated_texts):
            current = json_data
            for step in path[:-1]:  # Идем по пути до предпоследнего элемента
                current = current[step]
            current[path[-1]] = translated_text  # Заменяем последний элемент
            print(f"Замена по пути {path}: {translated_text}")

    return json_data, len(paths_to_translate), len(translated_texts)

def main(input_file, source_lang, target_lang, max_workers=10):
    print(f"Чтение файла: {input_file}")
    # Читаем JSON файл
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        print("Файл успешно загружен.")
    except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден.")
        return
    except json.JSONDecodeError:
        print(f"Ошибка: Файл {input_file} не является корректным JSON.")
        return

    # Обрабатываем JSON данные
    print("Обработка JSON данных...")
    processed_json_data, total_strings, translated_strings = process_json(json_data, source_lang, target_lang, max_workers)
    print("Обработка JSON данных завершена.")

    # Сохраняем результат в файл output.json в той же папке, где находится скрипт
    output_file = os.path.join(os.path.dirname(__file__), 'output.json')
    print(f"Запись результата в файл: {output_file}")
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(processed_json_data, file, ensure_ascii=False)
        print(f"Перевод завершен. Результат сохранен в файл: {output_file}")
    except Exception as e:
        print(f"Ошибка при записи файла {output_file}: {e}")

    # Вывод информативных результатов
    print("\nИнформативные результаты:")
    print(f"Всего строк для перевода: {total_strings}")
    print(f"Всего переведено строк: {translated_strings}")
    print(f"Файл с переведенными данными сохранен в: {output_file}")
    print("Процесс завершен.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Переводчик JSON файлов.")
    parser.add_argument('input_file', help="Имя входного JSON файла.")
    parser.add_argument('--source_lang', required=True, help="Язык, с которого переводим, например, zh-CN или ru.")
    parser.add_argument('--target_lang', required=True, help="Язык, на который переводим, например, en.")
    parser.add_argument('--max_workers', type=int, default=10, help="Максимальное количество параллельных задач (по умолчанию 10).")

    args = parser.parse_args()

    main(args.input_file, args.source_lang, args.target_lang, args.max_workers)