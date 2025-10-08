class ATM:
    def __init__(self,pin,amount=0,balance=10000):
        self.balance=balance
        self.amount=amount
        self.pin=pin
    def deposit(self):
       
        self.amount=amount=int(input("Enter deposit amount :"))
        balance=self.balance+self.amount
        print("your amount deposited !!")
        print(f"total amount is {balance}")
    def withdraw(self):
        amount=int(input("Enter withdraw amount :"))
        self.amount=amount
        while True:
            if(self.balance<self.amount):
                print("insufficent balance !!")
                self.amount=int(input("Enter withdraw amount again "))
            else:
                self.balance=self.balance-self.amount
                print(f"{amount}successfully withdrawed !!")
                print(f"remaining account balance is {self.balance}")
                break
               
    def checkbalance(self):
        print(f"your account balance is{ self.balance}")
    
    def changepin(self):
        pin=2005
        getpin=int(input("Enter your old pin :"))
        while True:
            if(pin==getpin):
                newpin=int(input("Enter your new pin:"))
                pin=newpin
                break
            else:
                print("incorrect old pin")
                continue
            
pin=2005
user=ATM(pin)
verify=int(input("Enter Your Pin Number :"))
while True:
    if(verify==pin):
        choice=input("choose option (1.Withdraw | 2.Deposit | 3.check balance | 4.change pin)")
        if(choice=="1"):
            user.withdraw()
        elif(choice=="2"):
            user.deposit()
        elif(choice=="3"):
            user.checkbalance()
        elif(choice=="4"):
            user.changepin()
        ask=input("agin or exit")
        if(ask=="again"):
            continue
        else:
            break
    else:
        print("incorrect pin ,Enter correct pin number ! ")
        continue
