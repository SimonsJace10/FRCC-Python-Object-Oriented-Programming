# Jace Simons FRCC CSC 233 Capstone Project - Graphics & Image Processing
# Exercise 2 - Red filter (Increase red level of each pixel by 30% in an image)
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
        bumped_red = round(red * 1.3)
        if bumped_red > 255:
            bumped_red = 255

        # set the pixel to have the new red value and keep the same blue and green values
        image.setPixel(row, col, bumped_red, green, blue)

# display the filtered image
window = GraphicsWindow()
canvas = window.canvas()
canvas.drawImage(image)
window.wait()
