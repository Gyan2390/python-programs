# calling multiple fn using nested fn
def calculator(num1, num2):

     def sum():
       return num1 + num2

     def sub():
        return num1 - num2

     def div():
        return num1 / num2

     def mul():
         return num1 * num2

     return sum, sub, div, mul

add_fn, sub_fn, div_fn, mul_fn  = calculator(4,5)

print(add_fn())
print(sub_fn())
print(div_fn())
print(mul_fn())