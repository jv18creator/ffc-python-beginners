from bank_accounts import BankAccount, InterestRewardsAcc, SavingAccount

Dave = BankAccount(1000, "Dave")
Jeet = BankAccount(2000, "Jeet")

Dave.get_balance()
Jeet.get_balance()

Jeet.deposit(20)
Dave.withdraw(1200)
Dave.withdraw(500)

Dave.transfer(10000, Jeet)
Dave.transfer(100, Jeet)

Jim = InterestRewardsAcc(1000, "Jim")
Jim.get_balance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingAccount(700, "Blaze")
Blaze.deposit(100)
Blaze.transfer(300, Jim)
