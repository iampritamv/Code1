class car:

    def __init__(self , brand , model):

        self.name = brand 
        self.model = model 
    
    def show(self):
        print(f"{self.name} {self.model}")

car1 = car("Tata" , "Nexon")
car1.show()