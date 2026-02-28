# 1 2 4 5

# Expected sum = 5*6/2 = 15
# Actual sum = 1+2+4+5 = 12
# Missing = 15-12 = 3


arr = list(map(int,input().split()))
         
size = int(input("Enter size"))

#1 sum = 0 
# for i in arr :

#     sum = sum + i

# ans = size * (size + 1)// 2

# print(ans-sum)

xor_all = 0 
xor_arr = 0 

for i in range(1 , size +1 ):

    xor_all ^= i

for num in arr :

    xor_arr ^=num

print(xor_all ^ xor_arr)


start = min(arr)
end = max(arr)

for i in range(start , end + 1 ):
    if i not in arr :
        print(i)