#Take input in List 1
list=input("enter element ").split()

print("list :" ,list)
print(type(list[0]))


#Take input in List 2
n = 5
list = []
for i in range(0 , n):
    element = int(input("enter element "))
    list.append(element)

print(list)
print(type(list[0]))