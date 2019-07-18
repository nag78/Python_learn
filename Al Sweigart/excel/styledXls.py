import openpyxl
from openpyxl.styles import Font

wb = openpyxl.Workbook()
sheet = wb.active
a = sheet.column_dimensions['A']
a.font = Font(size=24, italic=True)
a1 = sheet['A1'] = 'Здравствуй, мир!'
wb.save('styled.xlsx')
