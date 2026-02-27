list1 = [1 , 2 , 3 , 4 , 5 , 6]
c = 0
c1 = 0
for i in range(len(list1)):
    if list1[i] % 2 == 0 :
        c = c + 1     
    else:
        c1 = c1 + 1
print(" Even " , c) 
print(" odd " , c1)