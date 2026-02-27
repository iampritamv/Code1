def RotateLeftOne(arr , n):

    temp = arr[0]

    for i in range(0 , n-1):
        arr[i] = arr[i+1]

    arr[n-1]=temp
    
    return arr

n = 5
arr = [1,2,3,4,5]
print(RotateLeftOne(arr , n))