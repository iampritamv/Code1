class Employee:

    def __init__(self):

        self.name = "Pritam"
        self._email = "Pritam@gmail.com"
        self.__salary = 250000
    
    def show(self):
        print(f"email_id {self._email}")
        print(f"salary of the Employee {self.__salary}")


E2 = Employee()
print(E2.name)
#print(E2._email) ## allow but no recomanded
E2.show()
   