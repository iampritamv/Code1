def prime(n):
    count = 0
    for i in range(1 , n + 1):
        
        if(n % i == 0 ):

            count = count + 1
    if(count == 2):
        return True
    else:
        return False  
n = int(input("Enter a no : "))

if(prime(n) is True):
    print("It is a Prime no")
else:
    print("It is not a Prime no")

