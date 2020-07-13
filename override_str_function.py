# example of polymorphism in object oriented programming

class Account:
    def __init__(self, number, name, balance):
        self.account_number = number
        self.account_name = name
        self.account_balance = balance


def __str__(self):
        return "Account " + str(self.account_name) + " 's balance is " + str(self.account_balance)
     
acc = Account(1001, "MyAccountName", 100)
print(acc)