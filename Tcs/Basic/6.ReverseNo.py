#Reverse A no 

N = 123 
ans = 0

while N != 0 :

    Ldigit = N % 10 

    ans = ans*10 + Ldigit 

    N = N//10

print(ans)