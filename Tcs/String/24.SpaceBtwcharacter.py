s= input()
size=len(s)

result =""

for ch in s :

    if ch == s[0] and ch.isupper() :
        result = result + ch.lower()

    elif ch.isupper() :
        result = result + " " + ch.lower()
    
    else:
        result = result + ch

print(result)