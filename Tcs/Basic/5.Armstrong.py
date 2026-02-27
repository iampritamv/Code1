def Arms(N):
    temp = N 
    ans = 0
    d = len(str(N))

    while N != 0 :

        Ldigit = N%10 
        ans = ans + Ldigit ** d
        N = N//10

    if ans == temp :
        return True
    else :
        return False
    
n =  int(input(" Enter a no " ))

if Arms(n) :
    print("Arms")

else : 
    print("Not")