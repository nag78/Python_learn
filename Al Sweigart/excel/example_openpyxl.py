from openpyxl import load_workbook
wb = load_workbook(filename = 'example.xlsx')
sheets = wb.sheetnames
print(sheets)
