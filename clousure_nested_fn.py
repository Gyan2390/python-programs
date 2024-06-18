
# use- Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.

# print odd no. using closure
def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())

