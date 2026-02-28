# Equilibrium index = position where
# sum of left elements = sum of right elements

# 1 3 5 2 2

# 2

# Explanation
# Left sum = 1+3 = 4
# Right sum = 2+2 = 4


n = list(map(int , input().split()))
total = sum(n)

left = 0

for i in range(len(n)):
    right = total - left - n[i]

    if left == right :
        print(i)
        break

    left = left + n[i]

else:
    print("No equilibrium")