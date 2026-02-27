def BubbleSort(arr):

    size = len(arr)
    for i in range(0 , size):
        
        for j in range(0 , size-i-1):

            if arr[j] > arr[j+1] :
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [10 , 1 , 7 , 6 , 14 , 9]

print(BubbleSort(arr))