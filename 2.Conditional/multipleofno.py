def multiple(a , b , c , d , e , divisor):

    count = 0
    if a % divisor == 0:
        print(f"Multiple of {divisor}" , a)
        count = count + 1 
    if b % divisor == 0:
        print(f"Multiple of {divisor}" , b)
        count = count + 1 
    if c % divisor == 0:
        print(f"Multiple of {divisor}" , c)
        count = count + 1 
    if d % divisor == 0:
        print(f"Multiple of {divisor}" , d)
        count = count + 1 
    if e % divisor == 0:
        print(f"Multiple of {divisor}" , e)
        count = count + 1
    print()
    print(count , " multiples of 15 found")

a = int(input("Enter 1st no : "))
b = int(input("Enter 2nd no : "))
c = int(input("Enter 3rd no : "))
d = int(input("Enter 4th no : "))
e = int(input("Enter 5th no : "))

divisor = int(input("Enter divisor no : "))

multiple(a , b , c , d , e , divisor)