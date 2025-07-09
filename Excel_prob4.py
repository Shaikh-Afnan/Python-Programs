import openpyxl
import csv 
def csv2excel(csv_file,excel_file,delim = ','):
    data = list()
    with open(csv_file) as f:
        reader = csv.reader(f,delimiter= delim)
        for row in reader:
            data.append(row)
    # print(data)
    
    wb = openpyxl.Workbook()
    sheet = wb.active
    for row in data:
        sheet.append(row)

    wb.save(excel_file)

csv2excel('people3.csv','teacher.xlsx')