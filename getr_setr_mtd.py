
class cls:

    def __init__(self, temp):
        self.set_temp(temp)

    def increment(self):
        self.temp= self.temp+1

    def get_temp(self):
        return self.temp

    def set_temp(self, value):
        self.temp = value

clas = cls(45)

print(clas.get_temp())
clas.increment()
print(clas.get_temp())
clas.set_temp(200)
print(clas.get_temp())
clas.increment()
print(clas.get_temp())