
# my_list = int(input("list given: "))
list = [1,2,3,4,5]

for i in range (len(list) // 2):
    list[i], list[-i-1] = list[-i-1], list[i]

print(list)