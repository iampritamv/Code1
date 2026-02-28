arr = [ 1 , 2 ,300 ,48 ,5 ,6]
size = len(arr)

for i in range(size):
    for j in range(0 , size-i-1):

        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(*arr)

    