class Person:

    #constructor
    def __init__(self , name , age):
        
        self.name = name #instance attri
        self.age = age 

    def display(self):
        print(f"{self.name} {self.age}")

p1 = Person("Pritam",23)
# print(p1.name)
# print(p1.age)

p1.display()


