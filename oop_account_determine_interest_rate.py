class Account:
    def __init__(self, number):
        self.number = number
    
    def account_type(self):
        #  get the account type
        if str(self.number).startswith("1") :
            self.type = "current"
        elif str(self.number).startswith("2") :
            self.type = "savings"
    
    def interest_rate(self):
        
        self.account_type()
        if self.account_type == "current":
            self.interest = 0
        elif self.account_type == "savings":
            self.interest = 5
        return self.interest
     


acc = Account(2001)
acc.interest_rate()    

isinstance(acc, Account)   # returns True if acc is an instance of the class Account 