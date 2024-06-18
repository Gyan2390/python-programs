
import csv
csv.register_dialect('myDialect',
                     delimiter=',',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('C:\\Users\Admin\Downloads\customer.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='myDialect')
    for row in reader:
        print(row)