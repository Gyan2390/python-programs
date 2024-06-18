#011235
#01
#11
#12
#23
#35
num = int(input("no.of input locations: "))
a= 0
b= 1
print(a)
print(b)
for i in range(3,num+1):
    c=a+b
    # print(c)
    a=b
    b=c
    print(c)

# print