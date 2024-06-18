#the nonlocal keyword is used to declare that a variable inside a nested function (inner function) refers to a variable in the nearest enclosing (non-global) scope. This allows the inner function to modify the variable in the outer (enclosing) function.
# use -
# when you have nested functions and you need to modify a variable that is defined in the outer (enclosing) function from within the inner function.


def outer_function():
    outer_var = "Hello"

    def middle_function():
        middle_var = "World"

        def inner_function():
            nonlocal outer_var  # Refers to outer_var in outer_function
            outer_var = "Goodbye"
            nonlocal middle_var  # Refers to middle_var in middle_function
            middle_var = "Everyone"

        inner_function()
        print(middle_var)  # This will print "Everyone"

    middle_function()
    print(outer_var)  # This will print "Goodbye"

outer_function()
