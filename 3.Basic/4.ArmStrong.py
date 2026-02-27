n = 153 
dup = n
ans = 0
while(dup != 0):

    Ldigit = dup % 10

    ans = ans  + Ldigit ** 3

    dup = dup//10

if(n == ans ):
    print(f"{n} is a armstrong no")

else:
     print(f"{n} is not a armstrong no")