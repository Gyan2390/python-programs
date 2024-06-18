
class Animal:

    def __init__(self,name):
        self.name=name

    def sound(self):
        print("animal sound")

class Dog(Animal):

    def sound1(self):
        print("bark")

dog1= Dog("karan")
dog1.sound()
ani= Animal("shiv")
ani.sound()