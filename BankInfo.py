class Account:
    def _init_(self,in_balance,name):
        self.name=name
        self.balance= in_balance
        self.nominee =[]
        print("constructer called")


    def Deposit(self,deposit):
        self.balance = self.balance + deposit
        return self.balance

    def Withdrawal(self,withdraw):
        self.balance =self.balance - withdraw
        return self.balance

    def _eq_(self, other):
        return self.balance == other.balance

    def _gt_(self,other):
        return self.balance > other.balance

    def _ge_(self, other):
        return self.balance >= other.balance

    def _le_(self,other):
        return self.balance <= other.balance

    def AddNominee(self, val):
        self.nominee.append(val)

    def _len_(self):
        return len(self.nominee)

    def _getitem_(self, index):
        return self.nominee[index]