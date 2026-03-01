arr = list(map(int,input().split()))
         
size = int(input("Enter size"))
ans = sorted(arr)  
if ans == arr :
    print("Array is sorted")

else :
    print("Array is not sorted")

# M-2
# size=int(input())
# arr=[]

# for i in range(size):
#   ch = int(input())
#   arr.append(ch)

# arr2 = arr.copy()

# for i in range(size):
#   for j in range(0 , size - i - 1 ):
#     if arr2[j] > arr2[j + 1]:
#       arr2[j] , arr2[j+1] = arr2[j+1], arr2[j]


# if arr == arr2 :
#     print("sorted")
# else:
#     print("not sorted")