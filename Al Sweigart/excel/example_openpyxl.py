# -*- coding: cp1251 -*-

from openpyxl import load_workbook
wb = load_workbook(filename = 'example.xlsx')
sheet = wb.active
c = sheet['B1']
print('Строка ' + str(c.row) + ' Столбец ' + str(c.column) + ': ' +
      str(c.value))
time = sheet['A1'].value
print(time)

print('Ячейка ' + str(c.coordinate) + ' : ' + str(c.value))
