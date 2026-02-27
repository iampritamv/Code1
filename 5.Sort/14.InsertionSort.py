def InsertionSort(arr):
    n= len(arr)
    for i in range(0 , n):
    
        j=i

        while(j > 0 and arr[j-1] > arr[j] ):

            arr[j+1],arr[j] = arr[j],arr[j+1]


arr = [10 , 1 , 7 , 6 , 14 , 9]

print(InsertionSort(arr))
