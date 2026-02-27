for i in range( 0 , 5):

    #space
    for j in range(0 , i):
        print(" " , end = " ")
    
    for j in range(0 , 2*5 - (2*i+1)):
        print("*" , end = " ")
    
    for j in range(0 , i):
        print(" " , end = " ")
    
    print()
    