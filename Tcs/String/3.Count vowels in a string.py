n = input().lower()

v = 0
c = 0

for ch in n :
    if ch in 'aeiou' :
        v += 1
    if ch not in 'aeiou' :
        c += 1

print(v)
print(c)