def leap(year):

    if year % 4 == 0 :

        if year % 100 != 0 or year % 400 == 0 :
            return True

    return False

year = 2025
if leap(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")