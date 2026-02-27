def PerfNo(n):
    
    ans = 0 

    for i in range(1 , n):

        if n % i == 0 :

            ans = ans + i 
    
    if ans == n :
        return True
    else : 
        return False
    
n =  int(input(" Enter a no " ))

if PerfNo(n) :
    print("PerfectaNo")

else : 
    print("Not")