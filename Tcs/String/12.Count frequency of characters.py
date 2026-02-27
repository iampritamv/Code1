s= input("enter ")

freq = {}

for ch in s :
    if ch in freq :
        freq[ch] += 1
    else:
        freq[ch] = 1

for key in freq :
    print(f"{key}:{freq[key]}",end="")
