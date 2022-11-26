import turtle
import random

# Define width and height of the screen
width = 600
height = 400
width2 = width/2
height2 = height/2

# Create screen and turtle objects
screen = turtle.Screen()
screen.setup(width, height)
myTurtle = turtle.Turtle()
myTurtle.shape('turtle')

# Random walk
x, y = myTurtle.position()
while -width2<x<width2 and -height2<y<height2:    # Still in screen
    if random.randint(0, 1):
        myTurtle.left(90)
    else:
        myTurtle.right(90)
    myTurtle.forward(5)
    x, y = myTurtle.position()

screen.exitonclick()