# a1 = 1 2 3 4 5
# a2 = 3 4 5 6 7
# o/p - 3 4 5


arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

common = []

for num in arr1 :
    if num in arr2 and num not in common :
        common.append(num)
print(*common)
