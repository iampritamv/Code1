#2nd Largest element in array
n =int(input())

arr=[]

for i in range(n):
    num = int(input())
    arr.append(num)

arr.sort()
maxi = arr[-1]

for i in range(n-2, - 1 , -1):
    if arr[i] != maxi :
        second = arr[i]
        
print(second)
