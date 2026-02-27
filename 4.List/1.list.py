nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(nums)

maxi = -999
for i in range(0 , len(nums)):
    if(maxi < nums[i]):
        maxi = nums[i]

print(maxi)