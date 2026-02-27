def solve(arr , n):

    for i in range(1 , n):
        
        if(arr[i] < arr[i-1]):
            print("Arr is not sorted")
            return
    
    print("Arr is sorted")

n = 5
arr = [1,2,3,4,5]
solve(arr , n)