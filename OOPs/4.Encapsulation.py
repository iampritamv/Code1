class Atm : 

    def __init__(self , pin , balance):
        self.__pin = pin
        self.__balance = balance 

    def check_balance(self , pin):
        if pin == self.__pin :
            return f"Balance : {self.__balance}"
        
        else :
            return "Invalid Pin"
    
    def withdraw(self , pin , amount):
        if pin == self.__pin and amount<=self.__balance :
            self.__balance = self.__balance - amount
            return f"{amount} withdraw"

        else:
            return "Failed"
        

    def deposit(self , amount):
        if amount > 0 :

            self.__balance = self.__balance + amount  
            return f"Deposited ₹{amount}"

acc = Atm(1234, 1000)
results = []
# results.append(acc.check_balance(1234))
results.append(acc.deposit(5000))
print(results)
