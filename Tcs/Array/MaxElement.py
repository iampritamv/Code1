def Max(list1):
    
    maxi = float("-inf")

    for i in range(0 , len(list1)):
        if list1[i] > maxi :
            maxi = list1[i]

    return maxi


list1 = [ 1 , 2 ,300 ,48 ,5 ,6]
print(Max(list1))