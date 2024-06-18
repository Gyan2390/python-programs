
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2
        
def mul(dig):
    for num in dig:
        yield num*num

# print(sum(square(fibonacci_numbers(10))))
print(mul(square(fibonacci_numbers(10))))