# Jace Simons FRCC CSC 233 Capstone Project - Graphics & Image Processing
# Exercise 2 - Grayscale filter
# May 8, 2022

from ezgraphics import GraphicsImage, GraphicsWindow

# prompt user for filename
image_file = input("Input name of the image: ")

# load the file
image = GraphicsImage(image_file)

# do image processing

width = image.width()
height = image.height()

# iterate through the rows in the image
for row in range(height):
    # nested for loop: iterate through the columns
    for col in range(width):
        # get the red value of the current pixel being processed
        red = image.getRed(row, col)
        green = image.getGreen(row, col)
        blue = image.getBlue(row, col)

        # adjust value of red by increasing it by 30% up to 255
        fractional_red = round(red * 0.2126)
        fractional_green = round(green * 0.7152)
        fractional_blue = round(blue * 0.0722)
        gray = fractional_red + fractional_green + fractional_blue
        if gray > 255:
            gray = 255

        # set the pixel to have the new gray value for the r, g and b
        image.setPixel(row, col, gray, gray, gray)

# display the filtered image
window = GraphicsWindow()
canvas = window.canvas()
canvas.drawImage(image)
window.wait()
