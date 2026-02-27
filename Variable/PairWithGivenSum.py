# arr = [2, 7, 11, 15]
# target = 9

arr = list(map(int,input().split())) 
n = len(arr)
target = int(input(" enter target "))
for i in range(0 , n ):
    for j in range(i+1 , n ):
        if arr[i] + arr[j] == target :
            print(arr[i],arr[j])
