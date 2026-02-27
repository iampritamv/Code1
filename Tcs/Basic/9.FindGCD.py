# 👉 Factors of 12 → 1,2,3,4,6,12
# 👉 Factors of 18 → 1,2,3,6,9,18
# 👉 Highest common = 6

# import math

# First = int(input())
# Second = int(input())

# Gcd = math.gcd(First,Second)
# print(Gcd)

First = int(input())
Second = int(input())

while Second != 0 :
    First , Second = Second , First % Second

print(First) 
