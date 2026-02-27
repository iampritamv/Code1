def printf(n):
    
    if(n==0):
        
        return 1
    
    return n * printf(n - 1)



n = 5
print(printf(n))