def Prime(n):
    Count = 0
    for i in range(1 , Number+1) :
        if Number % i == 0 :
            Count = Count + 1
            if Count > 2 :
                break
        
        
    if Count == 2 :        
        return True
    else :
        return False

Number = int(input("Enter a no :"))

if Prime(Number):
    print("Prime")
else :
    print("Not Prime")





