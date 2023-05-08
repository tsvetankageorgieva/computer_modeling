import turtle

plane = turtle.Turtle()
screen = turtle.Screen()

# задаване на фон, който да е карта
screen.bgpic("map.gif")
screen.register_shape("plane2.gif")
screen.register_shape("marked.gif")

# задаване на форма на костенурката - самолет
plane.shape("plane2.gif")
plane.hideturtle()
planes = []

# задаване на мащаб 1:3км
scale = 3
# Въвеждане на данни за градовете - имена, разстояние, посока, градуси
list = [
    ["Прага", 1154, "северозапад", 315],
    ["Москва", 1751, "североизток", 32],
    ["Рим", 1083, "югозапад", 262],
    ["Истанбул", 361, "югоизток", 135],
]

for i in range(len(list)):
    planes.append(turtle.Turtle())
    planes[i].shape("plane2.gif")
    planes[i].hideturtle()
    # позициониране на пилота на самолета с лице към север
    planes[i].setheading(90)
    # преместване в началната точка - Велико Търново
    planes[i].penup()
    planes[i].goto(110, -150)
    planes[i].showturtle()
    planes[i].pendown()

    # завъртане в определена посока и изминаване на разстоянието
    planes[i].right(list[i][3])
    planes[i].speed(1)
    planes[i].forward(list[i][1]/scale)
    planes[i].shape("marked.gif")
plane.hideturtle()
# позициониране на пилота на самолета с лице към север
plane.setheading(90)
# преместване в началната точка - Велико Търново
plane.penup()
plane.goto(110, -150)
plane.showturtle()
plane.pendown()
