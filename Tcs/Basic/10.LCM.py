# 👉 Multiples of 4 → 4, 8, 12, 16…
# 👉 Multiples of 6 → 6, 12, 18…
# 👉 Smallest common = 12

import math

# First = int(input())
# Second = int(input())

# Lcm = math.lcm(First,Second)
# print(Lcm)

First = int(input())
Second = int(input())

lcm = abs(First*Second)//math.gcd(First,Second)
print(lcm)


