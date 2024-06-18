
# factorial using for loop
# num = int(input("no. of input: "))
# fact = 1
#
# for i in range(1,num+1):
#     # print(i)
#     fact = fact*i
#
# print(fact)

# # factorial using while
# num = int(input("no. of fact. ipt: "))
# fact = 1
#
# while num>1:
#     fact =  fact*num
#     num=num-1
#
# print(fact)

# factorial using via function

def factorial(n):
    if n<0:
        return "factorial is not defined for negative no.'s"

    fact=1

    while n>1:
        fact*=n
        n-=1

    return fact

number = int(input("factrial no.: "))
print(f"the factorial of {number} is {factorial(number)}")
