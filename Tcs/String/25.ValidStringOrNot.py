# ***###
# star = 3
# hash = 30
# o/p 0

s = input()

star = 0 
haash = 0

for ch in s :
    if ch == '*' :
        star += 1

    if ch == '#' :
        haash +=1

if star == haash :
        print(0)

else :
    print(star-haash)

