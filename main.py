class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.friends = 0
        self.account = BankAccount(int_rate=0.02, balance=0, bank="Wells Fargo")
    
    def make_friends(self):
        self.friends += 1
        return self

    def group_friends(self, amount):
        self.friends += amount
        return self
    
    def user_info(self):
        print(f"Username:{self.name} Age: {self.age} Num of Friends: {self.friends}")

class BankAccount:
    def __init__(self, int_rate, balance, bank):
        self.int_rate = int_rate
        self.balance = balance
        self.bank = bank

    def display_bank_info(self):
        print(f"Interest Rate: {self.int_rate}, Balance: {self.balance}, Bank: {self.bank}")


will = User("Will", 28)
shah = User("Shah", 28)
will.user_info()
will.account.display_bank_info()

chase = BankAccount(.02, 100, "Chase")
chase.display_bank_info()
# will.make_friends().group_friends(9).user_info()
# shah.user_info()
