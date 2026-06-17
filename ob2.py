class Bank :
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
    
    def debit(self,amount) :
        if amount > 0 and amount <= self.balance : 
            self.balance = self.balance - amount
            print("Rs", amount, "from account no", self.account, "was debited")
            print("Total Balance", self.get_bal())

    def credit(self,amount) : 
        if amount > 0 :
            self.balance = self.balance + amount
            print("Rs", amount, "from account no", self.account, "was credited")
            print("Total Balance", self.get_bal())

    def get_bal(self):
        return self.balance
acc1 = Bank(100000, 1220)
while True :
    print("""
            Welcome To The Bank!!!
          Options available ===>
            1. Credit
            2. Debit
            3. Exit""")
    choice = int(input()) 
    if choice == 1 :
        amount = int(input("Enter amount : "))
        acc1.debit(amount)

    elif choice == 2 :
        amount = int(input("Enter amount : "))
        acc1.debit(amount)

    elif choice == 3 :
        print("exciting...")
        break
    else :
        print("invalid option")
