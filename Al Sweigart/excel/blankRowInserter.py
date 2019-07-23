import sys
import openpyxl
from openpyxl import load_workbook

argument_1 = ''.join(sys.argv[1])
argument_2 = ''.join(sys.argv[2])
argument_3 = ''.join(sys.argv[3])
# argument_1 = 3
# argument_2 = 2
# argument_3 = 'multiple6.xlsx'
# print(argument_1)
# print(argument_2)
# print(argument_3)
# if argument_1 or argument_2 or argument_3 == '':
#     print('Проверте аргументы строки.')
# else:
wb = load_workbook(filename=str(argument_3))
ws = wb.active
# print(ws)
for i in range(int(argument_1)):
    ws.insert_rows(int(argument_2))
wb.save(filename=str(argument_3))
