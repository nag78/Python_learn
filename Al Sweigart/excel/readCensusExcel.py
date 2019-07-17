# -*- coding: cp1251 -*-

import openpyxl
from Lib.pprint import pprint


print('Открытие рабочей книги...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheets = wb.sheetnames
print(sheets)
sheet = wb[sheets[0]]
countyData = {}
# TODO: Заполнить словарь countyData данными о
# TODO: численности населения и
# TODO: переписных округов.

print('Чтение строк...')
for row in range(2, sheet.max_row + 1):
    # В каждой строке содержатся данные
    # для одного переписного района.
    state = sheet['B' + str(row)].value
    conty = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# TODO: Открыть новый текстовый файл и
# TODO: записать в него содержимое
# TODO: словоря countyData.
