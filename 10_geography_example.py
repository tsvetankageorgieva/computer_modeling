import turtle

# задаване на цветови модел RGB
turtle.colormode(255)

pen = turtle.Turtle()
screen = turtle.Screen()

# задаване на фон, който да е карта
screen.bgpic("map3.gif")
pen.fillcolor(255, 150, 255)
pen.pencolor(255, 100, 255)

vt = 66797 # брой население във Велико Търново
varna = 348668 # брой население във Варна
plovdiv = 364403 # брой население в Пловдив
burgas = 210813 # брой население в Бургас

# радиуса на кръга за Велико Търново
sum = vt + varna + plovdiv + burgas
r_vt = vt / sum * 100
r_varna = varna / sum * 100
r_plovdiv = plovdiv / sum * 100
r_burgas = burgas / sum * 100

# преместване в точка Велико Търново
pen.penup()
pen.goto(10, 85)
pen.pendown()
pen.begin_fill()
pen.circle(r_vt)
pen.end_fill()

# преместване в точка Варна
pen.penup()
pen.goto(360, 90)
pen.pendown()
pen.begin_fill()
pen.circle(r_varna)
pen.end_fill()

# преместване в точка Пловдив
pen.penup()
pen.goto(-145, -140)
pen.pendown()
pen.begin_fill()
pen.circle(r_plovdiv)
pen.end_fill()

# преместване в точка Бургас
pen.penup()
pen.goto(300, -65)
pen.pendown()
pen.begin_fill()
pen.circle(r_burgas)
pen.end_fill()
