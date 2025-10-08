class BankAccount:
    def __init__(self, account_number, account_holder, balance):
              self. account_number = account_number # Public
              self._account_holder = account_holder # Protected
              self.__balance = balance # Private

    def deposit(self, amount):
            if amount > 0:
                self.__balance += amount
                print(f"Deposited ₹{amount}. New Balance:   ₹{self.__balance}")
            else:
                print("Invalid deposit amount.")

    def withdraw(self, amount):
            if 0 < amount <= self. __balance:
                self. __balance -= amount
                print(f"Withdrew ₹{amount}. Remaining        Balance: ₹{self.__balance}")
            else:
                print("Insufficient funds or invalid amount.")


    def _display_holder_info(self):
        print(f"Account Holder: {self._account_holder}")

    def __apply_bank_charges(self):

        self.__balance -= 50
        print("₹50 bank charge applied.")
    def applycharge(self):
        account.__apply_bank_charges()


    def month_end_process(self):
            self.__apply_bank_charges()
            print("Month-end processing done.")



accno=int(input("Enter your accno:"))
name=input("Enter your name:")
amount=0
account = BankAccount(accno,name, amount)
while True:
    choice=input("Enter your choice (withdraw | deposit | info | charges | month end)")
    if(choice=="withdraw"):
        amount=int(input("Enter the amount you want withdraw :"))
        account.withdraw(amount)
    elif(choice=="deposit"):
        amount=int(input("Enter the amount you want deposit :"))
        account.deposit(amount)
    elif(choice=="info"):
       
        account._display_holder_info()
    elif(choice=="charges"):
       
        account.applycharge()
    else:
        print("invalid operation")
    choice2=input("again or close ?")
    if(choice2=="close"):
        break
    else:
        continue


