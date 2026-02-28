# 5
# 7 4 8 2 9

7 , 8 , 9


size=int(input())
arr=list(map(int,input().split()))
result = 1
maxi = arr[0]
for i in range(1 , size): 

    if arr[i] > maxi :
        result +=1
        maxi = arr[i]

print(result)