
import csv
path="C:\\Users\Admin\Downloads"

with open("C:\\Users\Admin\Downloads\customer.csv",'w',newline='') as file:
    writer=csv.writer(file, delimiter='/')
    writer.writerow(["shawn","30"])
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

with open("C:\\Users\Admin\Downloads\customer.csv",'r') as file:
    reader=csv.reader(file,quoting=csv.QUOTE_ALL,skipinitialspace=True,delimiter='/')

    for row in reader:
        print(row)

