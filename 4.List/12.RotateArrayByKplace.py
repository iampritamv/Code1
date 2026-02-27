def Rotate(arr , k):
    
    n = len(arr)
    newIndex = 0
    ans=[0] * n 
    for i in range(0 , n ):
        newIndex = (i + k) % n
        ans[newIndex]=arr[i]
    
    return ans



arr = [1 , 2 , 3, 4 ,5 ,6 ,7]
k = 3 
print(Rotate(arr , k))