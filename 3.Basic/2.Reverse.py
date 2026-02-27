n = 123 
ans=0
while(n):

    Ldigit = n % 10
    ans = (ans * 10) + Ldigit
    n = n//10

print(ans) 