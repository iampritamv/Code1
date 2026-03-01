#Find most frequent element
s = input()

freq = {}

for ch in s :
    if ch in freq :
        freq[ch] +=1
    else:
        freq[ch] = 1

# m = max(freq.values())

# for k in freq :
#     if freq[k] == m :
#         print(k,m)
#         break

maxi = float("-inf")
ans = None

for k, v in freq.items():
    if v > maxi:
        maxi = v
        ans = k

print(ans)