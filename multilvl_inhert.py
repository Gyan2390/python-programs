

class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)

class puppy(Dog):
    pass
    # def display(self):
    #     print("name: ",self.name)
# create an object of the subclass
# labrador = Dog()
pup = puppy()
# # access superclass attribute and method
# labrador.name = "Rohan"
# labrador.eat()

# call subclass method
# labrador.display()

pup.name="suzi"
pup.display()