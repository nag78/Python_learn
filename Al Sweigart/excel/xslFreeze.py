import openpyxl


wb = openpyxl.load_workbook('produceSales.xlsx')
ws = wb.active
ws.freeze_panes = 'A2'
wb.save('freezeExample.xslx')