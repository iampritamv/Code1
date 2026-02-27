class Employee:

    def work(self):
        print("Work in office")
    
class Devloper(Employee):

    def code(self):
        print("Write code")

dev = Devloper()
dev.code()
dev.work()
    