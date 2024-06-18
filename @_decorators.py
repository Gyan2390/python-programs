
def star(func):
    def inner(*args, **kwargs):
        name = kwargs.get('name')
        print(name * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        age = kwargs.get('age',0)
        for _ in range(15):
            print(age, end='')
        print()
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(**kwargs):
    name = kwargs.get('name')
    age = kwargs.get('age')
    print(f"{name}: {age}")

printer(name="saurav", age=20)