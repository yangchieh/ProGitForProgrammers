import turtle

# Create screen and turtle objects
screen = turtle.Screen()
screen.setup(500, 400)
screen.bgcolor('lightBlue')    # 淡藍色

myTurtle = turtle.Turtle()
myTurtle.shape('turtle')
myTurtle.color('orange')
myTurtle.pensize(3)    # 3 像素寬
myTurtle.penup()
myTurtle.goto(0, -100)
myTurtle.pendown()

# Move the turtle
for A in range(8):
  myTurtle.stamp()
  myTurtle.forward(75)
  myTurtle.left(45)

# Exit
screen.exitonclick()
