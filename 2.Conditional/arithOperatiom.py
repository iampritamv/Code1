def arithmetic(a , b , op):

    result = 0 
    if op == "+":
        result = a + b
    if op == "-":
        result = a - b
    if op == "/":
        result = a / b
    if op == "*":
        result = a * b
    
    print(a , op , b ,"=" ,result)

a = int(input("Enter 1st no : "))
b = int(input("Enter 2nd no : "))
op = input("Enter 1st no : ")

arithmetic(a , b , op)
