
class Vehicle:

    # name = ''
    def drive(self):
        print("driving vehicle")

class Four_wheeler:
    def driv(self):
        print("driving 4-wheeler")
        
class Car(Vehicle, Four_wheeler):
    pass

ford = Car()
ford.drive()
ford.driv()