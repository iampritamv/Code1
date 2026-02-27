def Fibo(n):

    a = 0 
    b = 1
    if(n == 0):
        return a

    for i in range(2 , n + 1 ):
        c = a + b
        a = b 
        b = c
    return b

n = int(input(" Enter a last term :  "))

print(Fibo(n))

