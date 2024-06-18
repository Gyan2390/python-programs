
import csv
path="C:\\Users\Admin\Downloads"
with open("C:\\Users\Admin\Downloads\customer.csv",'r') as file:
    reader=csv.reader(file, delimiter= '|')

    for row in file:
        print(row)
