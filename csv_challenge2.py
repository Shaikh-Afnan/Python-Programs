
import csv

people = [
['Dan', 34, 'Bucharest'],
['Andrei',21, 'London'],
['Maria', 45, 'Paris']
]

with open ('people1.csv','w') as f:
    writer = csv.writer(f, delimiter=':',lineterminator='\n')
    for item in people:
        writer.writerow(item)

with open ('people1.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)