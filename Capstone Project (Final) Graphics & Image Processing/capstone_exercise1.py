# Jace Simons FRCC CSC 233 Capstone Project - Graphics & Image Processing
# Exercise 1 - Draw a spiral using EZGraphics
# May 8, 2022

from ezgraphics import GraphicsWindow

# create the blank canvas
window = GraphicsWindow(250, 250)
window.setTitle("Spiral")
canvas = window.canvas()

# draw the spiral
# outside most line
canvas.drawLine(25, 25, 25, 225)
canvas.drawLine(25, 225, 225, 225)
canvas.drawLine(225, 225, 225, 25)
canvas.drawLine(225, 25, 50, 25)

# second to outside
canvas.drawLine(50, 25, 50, 200)
canvas.drawLine(50, 200, 200, 200)
canvas.drawLine(200, 200, 200, 50)
canvas.drawLine(200, 50, 75, 50)

# third
canvas.drawLine(75, 50, 75, 175)
canvas.drawLine(75, 175, 175, 175)
canvas.drawLine(175, 175, 175, 75)
canvas.drawLine(175, 75, 100, 75)

# fourth
canvas.drawLine(100, 75, 100, 150)
canvas.drawLine(100, 150, 150, 150)
canvas.drawLine(150, 150, 150, 100)
canvas.drawLine(150, 100, 125, 100)

# fifth
canvas.drawLine(125, 100, 125, 125)

# draw until the user closes the window
window.wait()
