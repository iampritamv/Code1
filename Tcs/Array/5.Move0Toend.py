# 0 0 1 2 3
# 1 2 3 0 0

arr= list(map(int,input().split()))

result = []

for num in arr : 
    if num != 0 :
        result.append(num)

zero_c =arr.count(0)

result.extend([0] * zero_c)

print(*result)