
def palindrome(txt):
    length = len(s)
    return txt[:length] == txt[::-1]

s = input("enter the string \n")
if(palindrome(s)):
    print("It is palindrome")
else:
    print("It is not a palindrome")