import openpyxl
from openpyxl.styles import Font


font = Font(name='Calibri',
            size=24,
            bold=True,
            italic=True,
            vertAlign=None,
            underline='none',
            strike=False,
            color='FF000000')

wb = openpyxl.Workbook()
ws = wb.active
col = ws.column_dimensions['1']
ws['A1'].value = 'Здравствуй, мир!'
col.font = font
wb.save('styled.xlsx')
