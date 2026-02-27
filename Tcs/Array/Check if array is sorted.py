arr = list(map(int,input().split()))
         
size = int(input("Enter size"))
ans = sorted(arr)  
if ans == arr :
    print("Array is sorted")

else :
    print("Array is not sorted")