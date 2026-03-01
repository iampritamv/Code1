list1 = [ 1 , 2 ,300 ,48 ,5 ,6]

# for i in range(len(list1)-1 , -1 ,-1):
#     print(list1[i] , end= " ")
i = 0 
j = len(list1) - 1 
while i < j :

    list1[i] , list1[j] = list1[j] , list1[i]
    i=i+1
    j=j-1

print(list1)
