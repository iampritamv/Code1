
# def Palindrome(N):
    
#     n1 = N 

#     ans = 0

#     while n1 != 0 :

#         Ldigit = n1%10 

#         ans = ans*10 + Ldigit 

#         n1=n1//10

#     if ans == N :
#         return True
#     else :
#         return False
    
def Palindrome(N):
    return str(n) == str(n)[::-1]


n =  int(input(" Enter a no " ))

if Palindrome(n) :
    print("Palindrome")

else : 
    print("Not")