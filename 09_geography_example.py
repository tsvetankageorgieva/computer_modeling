import turtle

plane = turtle.Turtle()
screen = turtle.Screen()

# задаване на фон, който да е карта
screen.bgpic("map.gif")
screen.register_shape("plane2.gif")

# задаване на форма на костенурката - самолет
plane.hideturtle()
plane.shape("plane2.gif")

# позициониране на пилота на самолета с лице към север
plane.setheading (90)

# преместване в началната точка - Велико Търново
plane.penup()
plane.goto(110, -150)
plane.showturtle()
plane.pendown()

# завъртане на северозапад и изминаване на разстояние 400 стъпки (1200 км), мащаб 1:3км
plane.right(315 )
plane.speed(1)
plane.forward(1154/3)

# позициониране на пилота на самолета с лице към север
plane.setheading (90)
