a = int(input("Enter 1st no :"))
b = int(input("Enter 2nd no :"))
c = int(input("Enter 3rd no :"))

if (a > b):
    if (a > c):
        print("a is largest")
    else:
        print("c is largest")

elif (b > a):
    if (b > c):
        print("b is largest")
    else:
        print("c is largest")

else:
    print("c is largest")