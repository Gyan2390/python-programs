
class person:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'the person name: {self.name} and age: {self.age}')

    def update_age(self,new_age):
        self.age=new_age

    def update_name(self,new_name):
        self.name=new_name

human = person("vidhu",20)

human.display()
human.update_age(30)
human.display()
human.update_name("shubham")
human.display()
