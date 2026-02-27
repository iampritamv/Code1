
for i in range(0 , 5):

    #space
    for j in range(0 , 5 - i - 1):
        print(" ", end=" ") 
    
    #Star
    for j in range(0 , 2*i+1):
        print("*", end=" ")

    #space
    for j in range(0 , 5 - i - 1):
        print(" ", end=" ") 
    
    print()
