import turtle


def drawSquare(t, color, size):
    t.color(color)         # 小烏龜顏色
    for i in range(4):
        t.forward(size)    # 方形邊長 
        t.left(90)         # 左轉 90 度


screen = turtle.Screen()
screen.setup(700, 500)
screen.bgcolor('lightyellow')

myTurtle = turtle.Turtle()
myTurtle.shape('blank')    # 小烏龜沒有形狀
drawSquare(myTurtle, 'blue', 100)  # 呼叫函式，給一組參數

myTurtle.left(180)
myTurtle.penup()
myTurtle.forward(100)
myTurtle.pendown()
drawSquare(myTurtle, 'red', 200)  # 呼叫函式，給另一組參數

screen.exitonclick()