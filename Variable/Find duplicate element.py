# Input: 1 2 3 2 4 5 3
# Output: 2 3

arr = list(map(int,input().split()))
        
freq={}

for num in arr :
    if num in freq :
        freq[num] += 1

    else:
        freq[num] = 1

    if freq[num] == 2 :
        print(num,end=" ")

