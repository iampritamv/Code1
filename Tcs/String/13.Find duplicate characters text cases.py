s = input()
# dup=""
# ans=""
# for ch in s :

#     if ch not in  dup :
#         dup +=ch
#     else:
#         ans +=ch
# print(ans)

seen = set()
ans = set()

for ch in s :
    if ch in seen :
        ans.add(ch)
    else :
        seen.add(ch)
    
print(*ans)