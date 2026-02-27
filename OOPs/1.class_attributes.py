class car:

    wheels = 4 #class attri(shared by all)

car1=car()
car2=car()
car2.wheels=6
print(car1.wheels)
print(car2.wheels)
