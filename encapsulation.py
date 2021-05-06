class BankAccount:
    _money = 0

    def deposit(self, money, password):
        if (authenticate(password)):
            self.money += money

    def withdraw(self, money, password):
        if (authenticate(password)):
            self.money -= money