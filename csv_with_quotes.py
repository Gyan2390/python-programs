import csv

path = "C:\\Users\Admin\Downloads"

with open('C:\\Users\Admin\Downloads\customer.csv','r') as file:
        reader = csv.reader(file, quoting= csv.QUOTE_ALL, skipinitialspace=True, delimiter='/')

        for row in reader:
            print(row)