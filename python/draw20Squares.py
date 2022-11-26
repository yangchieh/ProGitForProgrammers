import turtle

def drawColorSquare(t, size):
    for color in ['red', 'blue', 'orange', 'green']:
        t.color(color)
        t.forward(size)
        t.left(90)

screen = turtle.Screen()               # 設定螢幕與特性
screen.setup(800, 600)

myTurtle = turtle.Turtle()             # 產生小烏龜
myTurtle.pensize(2)
myTurtle.speed(10)

size = 20                              # 最小正方形的尺寸
for i in range(20):
    drawColorSquare(myTurtle, size)
    size += 10                         # 每次增加方形尺寸
    myTurtle.forward(10)               # 往前走 10 步
    myTurtle.right(18)                 # 右轉 10 度

screen.exitonclick()