# Въвеждане на време и скорост
t = float(input("Въведете време:"))
while t <= 0:
    t = float(input("Въведете време:"))
tm = input("Въведете мерната единица на времето (s, min, h):")
v = float(input("Въведете скорост:"))
while v <= 0:
    v = float(input("Въведете скорост:"))
vm = input("Въведете мерната единица на скоростта (m/s, km/h):")
# Функция за пресмятане на изминатия път
def compute_s(t, v):
    if tm == "s":
        t = t/3600
    elif tm == "min":
        t = t/60

    if vm == "m/s":
        v = v * 3.6
    s = t * v
    return s
print("Пътят е (в km/h): ", compute_s(t, v))

