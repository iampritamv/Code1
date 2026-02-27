arr = list(map(int,input().split())) # 5 , 6 , 7 , 8 
n = len(arr)
first=arr[0] 

for i in range(0 , n-1):
    arr[i] = arr[i+1]

arr[-1]=first

print(*arr)
