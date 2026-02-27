#Factorial of number

def Fact(n):
    ans = 1 
    for i in range(1 , n + 1):
        ans = ans * i #5 * 1

    return ans

Number = int(input("Enter Number "))
print(Fact(Number))
