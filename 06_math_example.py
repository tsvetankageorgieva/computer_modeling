# Пресмятане на лице на кръг и дължина на окръжност; изчертаване на окръжност, запълване на кръг с цвят
import turtle
pen = turtle.Turtle()

# константата 3.14
pi = 3.14
# задаване на радиус на окръжност
r = float(input("Въведете дължината на радиуса в cm (между 1 и 10):"))
while r <= 0:
    r = float(input("Въведете дължината на радиуса в cm (между 1 и 10):"))

# функция за пресмятане на дължината на окръжността
def C (r):
    C =  2 * pi * r
    return C
# функция за пресмятане на лицето на кръга
def S (r):
    r2 = r**2
    S =  pi * r2
    return S

print("Дължината на окръжността е", C(r))
print("Лицето на кръга е", S(r))

# изчертаване на окръжността и запълване на кръга
r = r * 20
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(r)
pen.end_fill()
pen.penup()
pen.goto(0, r)
pen.write("O", align="left")
pen.pendown()
pen.circle(0.5)
pen.hideturtle()
