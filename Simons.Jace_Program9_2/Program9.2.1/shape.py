class Shape:
    def __init__(self, color="green", filled=True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color: " + self.__color + " and filled: " + str(self.__filled)

## test Shape
##def main():
##    someShape = Shape()
##    otherShape = Shape("blue", False)
##
##    print(someShape.getColor())
##    print(otherShape.getColor())
##    print(someShape)   # calls the __str__() function
##    print(otherShape)  # calls the __str__() function
##
##
##main()
