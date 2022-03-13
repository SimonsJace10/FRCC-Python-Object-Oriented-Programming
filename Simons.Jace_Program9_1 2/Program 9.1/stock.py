"""
stock.py holds the class Stock which contains symbol, name, previous price and current price
"""


class Stock:
    """Represents a stock."""

    def __init__(self, symbol, name, previous_closing_price, current_price):
        """ The constructor instantiates member variables to passed in parameters"""
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previous_closing_price
        self.__currentPrice = current_price

    def get_name(self):
        """ Returns the stock's name """
        return self.__name

    def get_symbol(self):
        """ Returns the stock's symbol """
        return self.__symbol

    def get_previous_price(self):
        """ Returns the stock's previous closing price """
        return self.__previousClosingPrice

    def get_current_price(self):
        """ Returns the stock's current price """
        return self.__currentPrice

    def set_previous_price(self, price_input):
        """ Sets the stock's previous price """
        self.__previousClosingPrice = float(price_input)

    def set_current_price(self, price_input):
        """ Sets the stock's current price """
        self.__currentPrice = float(price_input)

    def get_change_percent(self):
        """ Returns the percentage delta in price day over day """
        """ The diff var is set to the difference between the previous price and the current price """
        diff = self.__previousClosingPrice - self.__currentPrice
        """ Then, we divide the difference by the original number (previous closing price) and assign it to the decimal 
        percentage (denoting that its still in decimal form)"""
        decimal_percentage = diff/self.__previousClosingPrice
        """ Finally, we multiply the decimal percentage by 100 to get the true percentage """
        percentage = decimal_percentage * 100
        """ Then return the true percentage (rounded to 2 decimal places) """
        return "Percentage change day over day: " + str(round(percentage, 2)) + "%"
