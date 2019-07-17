from openpyxl import load_workbook
wb = load_workbook(filename = 'example.xlsx')
sheets = wb.sheetnames
print(sheets)

sheet = wb[sheets[2]]
print(sheet)
ts = type(sheet)
print(str(ts))
st = sheet.title
print(str(st))

anotherSheet = wb.active
st = anotherSheet.title
print(str(st))
