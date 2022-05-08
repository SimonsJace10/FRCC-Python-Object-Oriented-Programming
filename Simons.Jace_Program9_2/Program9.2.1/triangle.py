# triangle.py holds the class triangle which contains sides 1 2 adnd 3 fields, and getter and setter methods for them.
# additionally, the class contains getArea and getPerimeter methods.

from shape import Shape


# the triangle class inherits methods from the Shape class
class Triangle(Shape):

    def __init__(self, side1, side2, side3):
        # call the init method for the parent class (from Shape)
        super().__init__()

        # initialize member vars
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    # Mutator Methods

    def set_side1(self, input_side1):
        self.__side1 = input_side1

    def set_side2(self, input_side2):
        self.__side2 = input_side2

    def set_side3(self, input_side3):
        self.__side3 = input_side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

    # Triangle Methods

    def get_perimeter(self):
        perimeter = self.__side1 + self.__side2 + self.__side3
        return perimeter

    def get_area(self):
        area = .5 * (self.__side1 * self.__side2)
        return area

    # readout of triangle

    def __str__(self):
        # calls the str readout of the Shape class which prints out color information
        super().__str__()
        # append the dimensional characteristics
        return "side 1: " + str(self.__side1) + "\nside 2: " + str(self.__side2) + "\nside 3: " + str(self.__side3)
