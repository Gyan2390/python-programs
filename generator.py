
def my_gen(n):
    value=0
    while value<n:
        yield value
        value+=1

for value in my_gen(5):
    print(value)