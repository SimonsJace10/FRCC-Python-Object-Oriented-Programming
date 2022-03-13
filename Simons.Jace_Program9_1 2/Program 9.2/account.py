"""
stock.py holds the class Stock which contains symbol, name, previous price and current price
"""


class Account:
    """Represents a stock."""

    def __init__(self, account_id, balance, annual_interest_rate):
        """ The constructor instantiates member variables to passed in parameters"""
        """ The values default to 0, 100 and 0 respectively, so if no values are provided, we can default to 0"""
        self.__account_id = 0
        self.__balance = 100
        self.__annual_interest_rate = 0
        self.__account_id = account_id
        self.__balance = balance
        """ we divide the inputted percentage by 100 to get to a decimal value """
        self.__annual_interest_rate = annual_interest_rate

    """ Accessor methods """
    def get_account_id(self):
        """ Returns the account's id """
        return self.__account_id

    def get_balance(self):
        """ Returns account balance """
        return self.__balance

    def get_annual_interest_rate(self):
        """ Returns annual interest rate """
        return self.__annual_interest_rate

    """ Mutator methods """
    def set_account_id(self, input_id):
        """ Set the account id """
        self.__account_id = input_id

    def set_balance(self, input_balance):
        """ Set the account balance """
        self.__balance = input_balance

    def set_annual_interest_rate(self, input_annual_interest_rate):
        """ Set annual interest rate """
        self.__annual_interest_rate = input_annual_interest_rate

    def get_monthly_interest_rate(self):
        """ Returns monthly interest rate """
        """ Since the annual interest rate is a percentage, we divide it by 100 before returning it """
        return (self.__annual_interest_rate/100) / 12

    def get_monthly_interest(self):
        """ Calculates and returns the monthly interest """
        return self.__balance * self.get_monthly_interest_rate()

    def withdraw(self, input_withdrawal):
        """ Withdraw a given amount of money from the account """
        self.__balance -= input_withdrawal

    def deposit(self, input_deposit):
        """ Depoist a given amount of money into the account """
        self.__balance += input_deposit
