# Отделяне на цифрите от естествени числа и намиране на сбора им
import random

# Получаване на естествено число, генерирано по случаен начин
number = random.randint(0, 1000000000)

# преобразуване на числото в низ и намиране на неговата дължина
digit_count = len(str(number))
sum = 0
n = number
# намиране на цифрите и сбора им
for i in range(0, digit_count):
    digit = n % 10
    n = n // 10
    sum = sum + digit

# Извеждане на числото и сбора на цифрите му
print("Сборът от цифрите на", number, "е", sum)
