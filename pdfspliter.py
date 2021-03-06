#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nag
#
# Created:     22.11.2018
# Copyright:   (c) Nag 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from appJar import gui
from PyPDF2 import PdfFileWriter, PdfFileReader
from pathlib import Path

# Определение всех необходимых для обработки файла функций

def split_pages(input_file, page_range, out_file):
    """ Использует PDF файл и копирует диапазон страниц в новый PDF файл

    Аргументы:
        input_file: Исходный PDF файл
        page_range: Строка, содержащая число копируемых страниц: : 1-3,4
        out_file: Название назначаемого PDF файла
    """
    output = PdfFileWriter()
    input_pdf = PdfFileReader(open(input_file, "rb"))
    output_file = open(out_file, "wb")

    # https://stackoverflow.com/questions/5704931/parse-string-of-integer-sets-with-intervals-to-list
    page_ranges = (x.split("-") for x in page_range.split(","))
    range_list = [i for r in page_ranges for i in range(int(r[0]), int(r[-1]) + 1)]

    for p in range_list:
        # Необходимо вычесть 1, так как страницы индексируются как 0
        try:
            output.addPage(input_pdf.getPage(p - 1))
        except IndexError:
            # Уведомляет пользователя и прекращает добавление страниц
            app.infoBox("Info", "Range exceeded number of pages in input.\nFile will still be saved.")
            break
    output.write(output_file)

    if(app.questionBox("File Save", "Output PDF saved. Do you want to quit?")):
        app.stop()


def validate_inputs(input_file, output_dir, range, file_name):
    """ Проверяем, если введенные пользователем значения являются правильными.

    Аргументы:
        input_file: Исходный PDF файл
        output_dir: Директория для хранения готового файла
        range: File Строка, содержащая число копируемых страниц: : 1-3,4
        file_name: Имя вывода готового PDF файла

    Возвращает:
        True, если ошибка и False, если нет
        Список сообщений об ошибке
    """
    errors = False
    error_msgs = []

    # Проверяет, выбран ли PDF файл
    if Path(input_file).suffix.upper() != ".PDF":
        errors = True
        error_msgs.append("Please select a PDF input file")

    # Проверяет, выбран ли диапазон
    if len(range) < 1:
        errors = True
        error_msgs.append("Please enter a valid page range")

    # Проверяет действительный каталог
    if not(Path(output_dir)).exists():
        errors = True
        error_msgs.append("Please Select a valid output directory")

    # Проверяет название файла
    if len(file_name) < 1:
        errors = True
        error_msgs.append("Please enter a file name")

    return(errors, error_msgs)


def press(button):
    """ Выполняет нажатие кнопки

    Аргументы:
        button: название кнопки. Используем названия Выполнить или Выход
    """
    if button == "Process":
        src_file = app.getEntry("Input_File")
        dest_dir = app.getEntry("Output_Directory")
        page_range = app.getEntry("Page_Ranges")
        out_file = app.getEntry("Output_name")
        errors, error_msg = validate_inputs(src_file, dest_dir, page_range, out_file)
        if errors:
            app.errorBox("Error", "\n".join(error_msg), parent=None)
        else:
            split_pages(src_file, page_range, Path(dest_dir, out_file))
    else:
        app.stop()


# Создать окно пользовательского интерфейса
app = gui("PDF Splitter", useTtk=True)
app.setTtkTheme("default")
app.setSize(500, 200)

# Добавить интерактивные компоненты
app.addLabel("Choose Source PDF File")
app.addFileEntry("Input_File")

app.addLabel("Select Output Directory")
app.addDirectoryEntry("Output_Directory")

app.addLabel("Output file name")
app.addEntry("Output_name")

app.addLabel("Page Ranges: 1,3,4-10")
app.addEntry("Page_Ranges")

# Связать кнопки с функцией под названием press
app.addButtons(["Process", "Quit"], press)

# Запуск интерфейса
app.go()