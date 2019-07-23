import sys
from openpyxl import load_workbook

argument_1 = ''.join(sys.argv[1])
argument_2 = ''.join(sys.argv[2])
argument_3 = ''.join(sys.argv[3])

wb = load_workbook(filename=str(argument_3))
ws = wb.active

for i in range(int(argument_1)):
    ws.insert_rows(int(argument_2))
wb.save(filename=str(argument_3))
