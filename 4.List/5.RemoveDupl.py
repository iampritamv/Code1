list = [1 , 2 , 2 ,3 ,4 , 4, 5, 6, 6 , 6]
list1=[list[0]]
for i in range(1,len(list)):
        if(list[i] != list[i-1]):
                list1.append(list[i])

print(list1)