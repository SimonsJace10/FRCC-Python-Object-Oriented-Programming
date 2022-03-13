from account import Account

""" instantiate account1 object of type Account with the provided parameters """
account1 = Account(1122, 20000, 4.5)
account1.withdraw(2500)
account1.deposit(3000)
""" Print out attributes """
print("Account ID: " + str(account1.get_account_id()) + "\nBalance: " + str(account1.get_balance()) +
      "\nMonthly Interest rate: " + str(account1.get_monthly_interest_rate()) + "\nMonthly Interest: "
      + str(account1.get_monthly_interest()))
