def SelectionSort(arr):

    n = len(arr)
    for i in range(0 , n):
        miniIndex = i
        for j in range(i+1 , n):

            if(arr[j] < arr[miniIndex]):

                miniIndex = j
        # Swap the found minimum element with the first element
        arr[i] , arr[miniIndex] = arr[miniIndex] , arr[i] 

    return arr

arr = [10 , 1 , 7 , 6 , 14 , 9]

print(SelectionSort(arr))