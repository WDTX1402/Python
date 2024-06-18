class BankAccount:
    def __init__(self, bname, oname, accno, balan):
        self.bname = bname
        self.oname = oname
        self.accno = accno
        self.balan = balan

    def print_balan(self):
        return f"Your current balance is {self.balan}"
    
    def depositmoney(self, depo):
        if depo > 0:
            self.balan += depo
        else:
            print("Invalid input")

    def withdrawmoney(self,withd):
        if withd <= self.balan:
            self.balan -= withd
        else:
            print("Insufficient Balance")



    

bank1 = BankAccount("JP Morgan", "Mr.Bdolf", 42069, 5000)
print(bank1.print_balan())
bank1.depositmoney(500)
print(bank1.print_balan())
bank1.withdrawmoney(5001)
print(bank1.print_balan())
bank1.withdrawmoney(5001)
print(bank1.print_balan())

