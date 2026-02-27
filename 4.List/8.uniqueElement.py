list = [1 , 2 , 2 ,3 , 3 ,4 , 4, 6, 6 ]
ans = 0

for i in range(len(list)):
    ans = ans ^ list[i]

print(ans)