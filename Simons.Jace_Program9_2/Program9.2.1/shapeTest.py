from shape import Shape
from rectangle import Rectangle
from triangle import Triangle


def main():

    # test code for the rectangle and triangle classes

    # ~~ RECTANGLE TEST CODE ~~

    my_rectangle = Rectangle(20, 30)

    print(my_rectangle.__str__())

    my_rectangle.set_width(100)
    my_rectangle.set_height(200)

    print(my_rectangle.__str__())

    print("perimeter: " + str(my_rectangle.get_perimeter()) + "\narea: " + str(my_rectangle.get_area()))

    # ~~ TRIANGLE TEST CODE ~~

    my_triangle = Triangle(10, 20, 30)

    print(my_triangle.__str__())

    my_triangle.set_side1(50)
    my_triangle.set_side2(60)
    my_triangle.set_side3(70)

    print(my_triangle.__str__())

    print("perimeter: " + str(my_triangle.get_perimeter()) + "\narea: " + str(my_triangle.get_area()))


main()
