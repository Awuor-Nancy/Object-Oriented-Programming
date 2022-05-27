class Account:
    def __init__(self,acc_name,balance,acc_type,branch):
        self.acc_name = acc_name
        self.balance = balance
        self.acc_type = acc_type
        self.branch = branch
        # return f"Dear {self.acc_name} your {self.acc_type} account has {self.balance} on the branch{self.branch}"

    def withdraw(self,amount):
        self.amount = amount
        return f"Dear {self.acc_name} your {self.acc_type} account has {self.balance-amount} on the branch{self.branch}"

    def deposit(self,cash):
        self.cash = cash
        return f"Dear {self.acc_name} your {self.acc_type} account has {self.balance-cash} on the branch{self.branch}"
       








