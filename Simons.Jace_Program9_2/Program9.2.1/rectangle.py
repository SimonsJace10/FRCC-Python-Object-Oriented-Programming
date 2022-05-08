# rectangle.py holds the class rectangle which contains width and height fields, and getter and setter methods for them.
# additionally, the class contains getArea and getPerimeter methods.

from shape import Shape


# the rectangle class inherits methods from the Shape class
class Rectangle(Shape):

    def __init__(self, width, height):
        # call the init method for the parent class (from Shape)
        super().__init__()

        # set member vars
        self.__width = width
        self.__height = height

    # Mutator Methods

    def set_width(self, input_width):
        self.__width = input_width

    def set_height(self, input_height):
        self.__height = input_height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    # Rectangle Methods

    def get_perimeter(self):
        perimeter = (self.__width * 2) + (self.__height * 2)
        return perimeter

    def get_area(self):
        area = self.__width * self.__height
        return area

    # readout of rectangle

    def __str__(self):
        # calls the str readout of the Shape class which prints out color information
        super().__str__()
        # append the width and height characteristics
        return "width: " + str(self.__width) + "\nheight: " + str(self.__height)
