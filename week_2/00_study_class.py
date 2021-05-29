class Person:
    def __init__(self, param_name):
        print("I am created", self)
        self.name = param_name
    def talk(self):
        print("Hello! My name is",self.name)

person_1= Person("Jiwon")
print(person_1.name)
person_1.talk()
person_2 = Person("Tina")
print(person_2.name)
print(person_2)
