import openpyxl

wb = openpyxl.load_workbook('Sales.xlsx',data_only=True)

sheet = wb.active
items = list()

for row in sheet.values:
    items.append(row)

print(items)

vat_list = list()

for row in items[1:]:
    element = [row[0],row[1] * 0.15]
    vat_list.append(element)

wb.create_sheet('VAT')
sheet = wb['VAT']
sheet['a1'] = 'Years'
sheet['b1'] = 'vat'

for row in vat_list:
    sheet.append(row)

wb.save('sales_and_vat.xlsx')