#1. Size + space-separated array (MOST COMMON)

# 5
# 1 2 3 4 5

n = int(input())
arr = list(map(int , input().split()))

# print(*arr)

# 2. Size + elements in new lines

n = int(input())

arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

# print(*arr)

#3. Only array given (no size)
# 1 2 3 4 5

arr = list(map(int, input().split()))
n = len(arr)


# 4. Comma-separated input

1,2,3,4,5

arr = list(map(int, input().split(',')))

# 5. Bracket input (rare but possible)

[1,2,3,4,5]

s = input().strip()
s = s.strip('[]')
arr =  list(map(int, s.split(',')))