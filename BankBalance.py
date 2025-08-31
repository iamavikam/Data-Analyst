class BankBalance:
    def __init__(self, accountholdername, amount):
        self.accountholdername=accountholdername
        self.amount=amount

    def deposit(self,depamount):
        self.depamount=depamount
        if self.depamount>0:
            self.amount+=self.depamount
            print(f"Deposited amount is {self.depamount} and Total Balance is {self.amount}")
        else:
            print("Invalid deposit")
        #print(f"Final Amount of {self.accountholdername} is {self.amount}")
        self.get_balance()

    def withdrawal(self,withdrawalamt):
        self.withdrawamt=withdrawalamt
        if self.withdrawamt>0 and self.withdrawamt<self.amount:
            self.amount-=self.withdrawamt
            print(f"Withdrawl of {self.withdrawamt} done and Total Balance is {self.amount}")
        else:
            print("Invalid Withdrawal")
        self.get_balance()

    def get_balance(self):
        print(f"Final Amount of {self.accountholdername} is {self.amount}")

bankbalance=BankBalance(input("Enter Account Holder Name \n"),int(input("Enter Initial Amount \n")))
bankbalance.deposit(int(input("Enter Amount to Deposit \n")))
bankbalance.withdrawal(int(input("Enter Amount to Withdraw \n")))
