arr = list(map(int , input().split())) #-2 1 -3 4 -1 2 1 -5 4

maxi = arr[0]
csum =0 

for num in arr : 
    
    csum += num 

    if csum > maxi :
        maxi = csum

    if csum < 0 : 
        csum = 0 

print(maxi)