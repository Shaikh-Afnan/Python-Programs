import csv
import openpyxl
def excel2csv(excel_file,csv_file):
    wb = openpyxl.load_workbook(excel_file,data_only=True)
    sheet = wb.active
    with open(csv_file,'w') as f:
        writer = csv.writer(f)
        for row in sheet.values:
            writer.writerow(row)
                


excel2csv('books.xlsx','booklist.csv')