# ✅ Leap Year Rule

# A year is leap if:

# Divisible by 400 → Leap year ✅

# Divisible by 4 but NOT by 100 → Leap year ✅

# Otherwise → Not leap ❌

n = int(input())

if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print("Leap year")
else:
    print("Not Leap Year")