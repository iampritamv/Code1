class Car:

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

    
class Bmw(Car) :

    def __int__(self ,  name):
        self.name = name

Car1=Car()
Car.start()

Car2 = Bmw("IRIS")
print(Car2.name())
