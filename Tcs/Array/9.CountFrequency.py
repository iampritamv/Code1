#Count frequency of each element in array

# i/p 1 2 2 3 3 3 4
#o/p
# 1 → 1
# 2 → 2
# 3 → 3
# 4 → 1

arr = list(map(int,input().split()))

freq = {}

for num in arr : 
    if num in freq :
        freq[num] += 1

    else:
        freq[num] = 1

for key in freq :
    print(key , freq[key])

for k , v in freq.items():
    print(f"{k}->{v}")