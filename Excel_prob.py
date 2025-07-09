import openpyxl
from openpyxl.styles import *

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Company Sales'
entries = [('Years','Sales'),(2017,150000),(2018,180000),(2019,210000),(2020,125000)]
for entry in entries:
    sheet.append(entry)

sheet['b6'] = f'=sum(b2:b5)'
sheet['c6'] = 'Total Sales'

font = Font(name='Tahoma', size=10, color='ff0000', bold=True, italic=False)
cell = sheet['b6']
cell.font = font

cell_c6 = sheet['c6']
cell_c6.font = font


wb.save('Sales.xlsx')