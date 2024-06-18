

def calculator(func):

    def wrap(num1, num2):
        result  = func(num1,num2)
        print(f"Operation: {func.__name__} ({num1},{num2}) = {result}")
        return result
    return wrap

@calculator
def sum(num1, num2):
    return num1+num2

@calculator
def sub(num1, num2):
     return num1-num2

@calculator
def mul(num1, num2):
      return num1*num2

@calculator
def div(num1, num2):
    if num2==0:
        return "Error! division is zero."
    return num1/num2


print(sum(5,3))
print(sub(7,3))
print(mul(4,7))
print(div(8,4))

