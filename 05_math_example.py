# Изчертаване на графиката на права пропорционалност
# Изчертаване на координатна система
import turtle
pen = turtle.Turtle()
pen.hideturtle()
# Изчертаване на Ox
pen.penup()
pen.goto(-200, 0)
pen.pendown()
pen.goto(200, 0)
pen.write("x", align="left")
pen.penup()
# Изчертаване на стрелката на Ox
pen.goto(190,5)
pen.pendown()
pen.goto(200,0)
pen.penup()
pen.goto(190,-5)
pen.pendown()
pen.goto(200,0)
# Изчертаване на Oy
pen.penup()
pen.goto(0, -200)
pen.pendown()
pen.goto(0, 200)
pen.write("y", align="right")
# Изчертаване на стрелката на Oy
pen.goto(5,190)
pen.pendown()
pen.goto(0,200)
pen.penup()
pen.goto(-5,190)
pen.pendown()
pen.goto(0,200)
# Изписване на O
pen.penup()
pen.goto(-3,-18)
pen.write("O", align="right")
# Изчертаване на деления по осите
for i in range(1, 20):
    pen.penup()
    pen.goto(-(200-i*20), 3)
    pen.pendown()
    pen.goto(-(200-i*20), -3)
for i in range(1, 20):
    pen.penup()
    pen.goto(3, -(200-i*20))
    pen.pendown()
    pen.goto(-3, -(200-i*20))

# задаване на коефициент на пропорционалност
k = -1/2
# права пропорционалност
def f (x):
    y = k * x
    return y;

# изчертаване на права пропорционалност
x1 = -200
y1 = f(x1)
x2 = 200
y2 = f(x2)
pen.penup()
pen.goto(x1, y1)
pen.pendown()
pen.speed(1)
pen.goto(x2, y2)
