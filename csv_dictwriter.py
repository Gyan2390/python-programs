
import csv
path="C:\\Users\Admin\Downloads"
# a is appending here
with open("C:\\Users\Admin\Downloads\customer.csv",'a',newline='') as file:
    data = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=data)

    writer.writeheader()  
    writer.writerow({'name': 'gyan', 'age': 40})
    writer.writerow({'name': 'shubh', 'age': 30})
    writer.writerow({'name': 'shawn', 'age': 35})
