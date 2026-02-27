s = input()

seen = ""

for ch in s :
    if ch not in seen :
        seen += ch

print(seen)