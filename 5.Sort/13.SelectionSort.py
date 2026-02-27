def InsertionSort(arr):
    
    n = len(arr)
    for i in range(0 , n):
        temp = arr[i]
        for j in range(i-1 , -1 ,-1):

            if(arr[j] > temp):

                arr[j+1] = arr[j]
            else:
                break
        arr[j+1]= temp




arr = [10 , 1 , 7 , 6 , 14 , 9]

print(InsertionSort(arr))