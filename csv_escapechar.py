

import csv
row_list = [
    ['Book', 'Quote'],
    ['Lord of the Rings',
     '"All we have to decide is what to do with the time that is given us."'],
    ['Harry Potter', '"It matters not what someone is born, but what they grow to be."']
]
# csv.register_dialect('myDialect',
#                      delimiter='|',
#                      quoting=csv.QUOTE_ALL)
with open('C:\\Users\Admin\Downloads\customer.csv', 'w', newline='') as file:
    writer = csv.writer(file, escapechar='/', quoting=csv.QUOTE_NONE)
    writer.writerows(row_list)
    for row in row_list:
        print(row)