n = 121
ans = 0

duplicate = n
while(duplicate):

    lastdigit = duplicate % 10 

    ans = ans * 10 + lastdigit

    duplicate = duplicate // 10 

if(n == ans):
    print("It is a palindrome Numb")

else:
    print("It is not a palindrome Numb")