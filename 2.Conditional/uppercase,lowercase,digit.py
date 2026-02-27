def check(ch):

    if ch.isdigit() :
        print("The Character you entered is Digit")

    if ch >= "A" and ch <="Z" :
        print("The Character you entered is UpperCase")

    else :
        print("The Character you entered is LowerCase")

ch = input(" Enter the Character : ")
print()

check(ch)