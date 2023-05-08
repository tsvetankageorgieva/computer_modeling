import turtle

# задаване на цветови модел RGB
turtle.colormode(255)

pen = turtle.Turtle()
screen = turtle.Screen()

# задаване на фон, който да е карта
screen.bgpic("map3.gif")
pen.fillcolor(255, 150, 255)
pen.pencolor(255, 100, 255)

# Въвеждане на данни за градове и брой население
list = [
    ["Велико Търново", 348668, [10, 85]],
    ["Варна", 348668, [360, 90]],
    ["Пловдив", 364403, [-145, -140]],
    ["Бургас", 210813, [300, -65]],
]

# радиусите на кръговете за градовете
sum = 0
for i in range(len(list)):
    sum = sum + list[i][1]
r_circles = []
for i in range(len(list)):
    r_circles.append(list[i][1] / sum * 100)

    # преместване в точка поредния град
    pen.penup()
    pen.goto(list[i][2][0], list[i][2][1])
    pen.pendown()
    pen.begin_fill()
    # изчертаване на кръг
    pen.circle(r_circles[i])
    pen.end_fill()
