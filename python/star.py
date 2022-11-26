import turtle

screen = turtle.Screen()
screen.setup(400, 300)

myTurtle = turtle.Turtle()
myTurtle.color('red', 'yellow')    # 多邊形外框紅色，內部區域黃色
myTurtle.speed(10)                 # 設定速度
myTurtle.backward(100)             # 後退 100 (讓圖形置中)

myTurtle.begin_fill()    # 開始填色
for i in range(36): 
    myTurtle.forward(200)
    myTurtle.left(170)
myTurtle.end_fill()      # 結束填色

screen.exitonclick()
