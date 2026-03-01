# 4 5 1 2 0 4 1 0

# 5

n = int(input())

arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

freq = {}

# count frequency
for ch in arr:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# find first non-repeating in array order
for num in arr:
    if freq[num] == 1:
        print(num)
        break
else:
    print("No non-repeating element")