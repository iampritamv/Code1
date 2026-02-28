# 0 0 1 0 1 1 0

# 6

# (Subarray: 0 1 0 1 1 0)


arr = list(map(int , input().split()))
size = len(arr)
max_len = 0
for i in range(size):
    zero = one = 0
    for j in range(i , size ):
        if arr[j]==0 :
            one +=1

        else :
            zero +=1 

        if zero == one :
            max_len = max(max_len , j - i + 1 )

print(max_len)