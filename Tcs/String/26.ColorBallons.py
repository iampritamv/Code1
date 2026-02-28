# n = int(input())

# arr = []

# for i in range(n):
#     e = input().strip() 
#     arr.append(e)
arr = ['r','g','b','b','g','y','y']
freq = {}
for ch in arr :
    if ch in freq :
        freq[ch] += 1

    else :
        freq[ch] = 1

for k,v in freq.items():
    if v % 2 != 0 :
        print(k)

# for k,v in freq.items():
#     print("Key:", k, "Value:", v)
# print(freq)
