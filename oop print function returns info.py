class Account:
    def __init__(self, number, name, balance):
        self.account_number = number
        self.account_name = name
        self.account_balance = balance


acc = Account(1001, "MyAccountName", 100)
print(acc)

#  result is <__main__.Account object at 0x1057f4c10>