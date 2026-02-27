print("Welcome to tip calculator !")

bill = float(input("Enter total bill ?"))

tip = float(input(" amount --> 10 , 12 ,15 ?"))


spilt = float(input("How many people to spilt"))


total = (bill + tip) / spilt

total1 = round(total,2)
print(f"Each person should pay : {total1}")
