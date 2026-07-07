class ATM:
    

    def __init__(self):
        self.pin = "1234"
        self.balance= 1000
        self.withdraw = ()
        self.history = []

    def atm_info(self,user_pin):
        if user_pin == self.pin:
            print(f"pin is correct :{self.pin}")
        else:
            print("invild pin")


    def deposite(self):
        amount = int(input("entre a amount:"))

        if amount >= 0:
            self.balance +=amount
            self.history.append(f"deposite amount{amount}")
            print(f"transaction is sucessfull done ✅{slef.balance}")

        else :
            print("ivild amount")


    def withdraw(self):
        print(f"this blance of your acc {self.balance}")
        amount = float(input("entre a withdraw amount : "))
        if amount <= self.deposite :
            self.deposite -= amount
            self.history.append(f"withdraw amont is {amount}")
            print(f"remandinf balance = {self.balance}")

        else :
            print("insufficient balance ,current balance is{self.balance}")


    def transaction_history(self):
        print("-----------transaction history here----------")

        if len(self.history) == 0 :
            print("no transaction yet")

        else :
            for transaction in self.history:
                print(transaction)
     

            
atm = ATM()

print("===== welcome to python ATM =====")

user_pin = input("Entre a pin number =")

if atm.atm_info(user_pin):
    while true:
        print("\n===== MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transaction History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.deposit()

        elif choice == "2":
            atm.withdraw()

        elif choice == "3":
            atm.transaction_history()

        elif choice == "4":
            print(" Thank you for using Python ATM.")

        else:
            print(" Invalid Choice!")






















    
        
        
        
    
        
   






        
               
        
