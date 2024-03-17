class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initial_amount, amount_name) -> None:
        self.balance = initial_amount
        self.name = amount_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, aacount '{self.name}' only has balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.. ")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. {error}")


class InterestRewardsAcc(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete")
        self.get_balance()


class SavingAccount(InterestRewardsAcc):
    def __init__(self, initial_amount, amount_name) -> None:
        super().__init__(initial_amount, amount_name)
        self.fee = 2

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
