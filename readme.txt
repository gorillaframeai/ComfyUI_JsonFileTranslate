Instructions for Using the JSON File Translation Script

1. Install Python
Ensure you have Python version 3.11.9 or higher installed. You can download and install Python from the official website:
https://www.python.org/downloads/

2. Install Dependencies
To run the script, you need to install the following dependencies:
- deep-translator: Library for text translation.
- argparse: Library for command-line argument parsing (already included in the standard Python library).

To install the necessary dependencies, run the following command in the command line or terminal:
pip install deep-translator
or run the requirements.txt file:
pip install -r requirements.txt

3. Prepare the JSON File
Prepare the JSON file you want to translate. Ensure the file is in correct JSON format and contains the strings to be translated.

4. Run the Script
To run the script, use the command line or terminal. Navigate to the directory where the script is located and execute the following command:
python jsontransate_lang.py <input_file> --source_lang <source_lang> --target_lang <target_lang> --max_workers <max_workers>

Where:
- <input_file>: Path to the input JSON file to be translated.
- <source_lang>: The language from which to translate the text. Possible values:
  - en: English
  - ja: Japanese
  - zh-CN: Chinese (Simplified)
  - ru: Russian
- <target_lang>: The language to which to translate the text. Possible values:
  - en: English
  - ja: Japanese
  - zh-CN: Chinese (Simplified)
  - ru: Russian
- <max_workers>: The maximum number of parallel tasks for translation (default is 10). This parameter is optional.


Example Usage
Assume you have a JSON file named data.json that you want to translate from Chinese to English, and you want to use 10 parallel tasks for the translation. Run the following command:
python jsontransate_lang.py data.json --source_lang zh-CN --target_lang en --max_workers 10 

5. Results
After the script completes execution, you will see informative messages in the console that help you understand what was done:
- The total number of strings to be translated.
- The total number of translated strings.
- The path to the file with the translated data.

The translated data will be saved in the file output.json in the same directory as the script.

---

Инструкция по использованию скрипта для перевода JSON файлов

1. Установка Python
Убедитесь, что у вас установлен Python версии 3.11.9 или выше. Вы можете скачать и установить Python с официального сайта:
https://www.python.org/downloads/

2. Установка зависимостей
Для работы скрипта необходимо установить следующие зависимости:
- deep-translator: Библиотека для перевода текста.
- argparse: Библиотека для обработки аргументов командной строки (уже включена в стандартную библиотеку Python).

Для установки необходимых зависимостей выполните следующую команду в командной строке или терминале:
pip install deep-translator
или запустите файл requirements.txt:
pip install -r requirements.txt

3. Подготовка JSON файла
Подготовьте JSON файл, который вы хотите перевести. Убедитесь, что файл имеет корректный формат JSON и содержит строки, которые нужно перевести.

4. Запуск скрипта
Для запуска скрипта используйте командную строку или терминал. Перейдите в директорию, где находится скрипт, и выполните следующую команду:
python jsontransate_lang.py <input_file> --source_lang <source_lang> --target_lang <target_lang> --max_workers <max_workers>

Где:
- <input_file>: Путь к входному JSON файлу, который нужно перевести.
- <source_lang>: Язык, с которого нужно перевести текст. Возможные значения:
  - en: Английский
  - ja: Японский
  - zh-CN: Китайский (упрощенный)
  - ru: Русский
- <target_lang>: Язык, на который нужно перевести текст. Возможные значения:
  - en: Английский
  - ja: Японский
  - zh-CN: Китайский (упрощенный)
  - ru: Русский
- <max_workers>: Максимальное количество параллельных задач для перевода (по умолчанию 10). Этот параметр является необязательным.


Пример использования
Предположим, у вас есть JSON файл data.json, который нужно перевести с китайского на английский, и вы хотите использовать 10 параллельных задач для перевода. Выполните следующую команду:
python jsontransate_lang.py data.json --source_lang zh-CN --target_lang en --max_workers 10 

5. Результаты
После завершения выполнения скрипта, вы увидите информативные сообщения в консоли, которые помогут вам понять, что было сделано:
- Общее количество строк для перевода.
- Общее количество переведенных строк.
- Путь к файлу с переведенными данными.

Переведенные данные будут сохранены в файл output.json в той же папке, где находится скрипт.

---

JSON文件翻译脚本使用说明

1. 安装Python
请确保已安装Python 3.11.9或更高版本。您可以从官方网站下载并安装Python：
https://www.python.org/downloads/

2. 安装依赖项
要运行脚本，您需要安装以下依赖项：
- deep-translator：用于文本翻译的库。
- argparse：用于命令行参数解析的库（已包含在Python标准库中）。

要安装所需的依赖项，请在命令行或终端中运行以下命令：
pip install deep-translator
或运行requirements.txt文件：
pip install -r requirements.txt

3. 准备JSON文件
准备好您想要翻译的JSON文件。确保文件是正确的JSON格式，并包含要翻译的字符串。

4. 运行脚本
使用命令行或终端运行脚本。导航到脚本所在的目录并执行以下命令：
python jsontransate_lang.py <input_file> --source_lang <source_lang> --target_lang <target_lang> --max_workers <max_workers>

其中：
- <input_file>：要翻译的输入JSON文件的路径。
- <source_lang>：要翻译的源语言。可能的值：
  - en：英语
  - ja：日语
  - zh-CN：简体中文
  - ru：俄语
- <target_lang>：要翻译的目标语言。可能的值：
  - en：英语
  - ja：日语
  - zh-CN：简体中文
  - ru：俄语
- <max_workers>：翻译的最大并行任务数（默认为10）。此参数是可选的。


示例用法
假设您有一个名为data.json的JSON文件，您希望将其从中文翻译成英文，并希望使用10个并行任务进行翻译。运行以下命令：
python jsontransate_lang.py data.json --source_lang zh-CN --target_lang en --max_workers 10 

5. 结果
脚本完成执行后，您将在控制台中看到有助于理解完成情况的信息消息：
- 要翻译的字符串总数。
- 已翻译的字符串总数。
- 包含翻译数据的文件路径。

翻译后的数据将保存在与脚本相同目录中的output.json文件中。