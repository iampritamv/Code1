class Car :

    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brake = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("CAR STARTED...")

car1 = Car()
car1.start()