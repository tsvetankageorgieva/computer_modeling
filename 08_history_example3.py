import turtle

event1 = turtle.Turtle()
event2 = turtle.Turtle()
event3 = turtle.Turtle()
event4 = turtle.Turtle()
event5 = turtle.Turtle()
screen = turtle.Screen()

# задаване на фон, който да е карта
screen.bgpic("timeline.gif")
screen.register_shape("event1.gif")
screen.register_shape("event2.gif")
screen.register_shape("event3.gif")
screen.register_shape("event4.gif")
screen.register_shape("event5.gif")

# преместване в точка на времевата линия, отговаряща на събитие 1
event1.penup()
event1.goto(-440, 80)
event1.showturtle()
event1.pendown()
# задаване на форма на костенурката - събитие 1
event1.shape("event1.gif")

# преместване в точка на времевата линия, отговаряща на събитие 2
event2.penup()
event2.goto(-10, 80)
event2.showturtle()
event2.pendown()
# задаване на форма на костенурката - събитие 2
event2.shape("event2.gif")

# преместване в точка на времевата линия, отговаряща на събитие 2
event3.penup()
event3.goto(80, -100)
event3.showturtle()
event3.pendown()
# задаване на форма на костенурката - събитие 3
event3.shape("event3.gif")

# преместване в точка на времевата линия, отговаряща на събитие 4
event4.penup()
event4.goto(150, 80)
event4.showturtle()
event4.pendown()
# задаване на форма на костенурката - събитие 4
event4.shape("event4.gif")

# преместване в точка на времевата линия, отговаряща на събитие 5
event5.penup()
event5.goto(400, 80)
event5.showturtle()
event5.pendown()
# задаване на форма на костенурката - събитие 5
event5.shape("event5.gif")
