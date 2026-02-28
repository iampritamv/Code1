arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

size = len(arr1)

#1 arr3 = []

# for num in arr1 : 
#     arr3.append(num)

# for num2 in arr2 : 
#     arr3.append(num2)


# arr3.sort()
# print(arr3)


arr3 = arr1 + arr2

ans = set(arr3)
print(ans)


unique = []
for num in arr3 :
    if num not in unique :
        unique.append(num)

print(*unique)