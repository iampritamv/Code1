s = input()

seen = ""

for ch in s :
    if ch not in "AEIOUaeiou" :
        seen += ch
print(seen)