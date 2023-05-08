# Намиране на простите делители между 1 и 20 на дадено число
# Създаване на списък с простите числа между 1 и 20
import random

primes = [2, 3, 5, 7, 11, 13, 17, 19]

# Получаване на цяло число, генерирано по случаен начин
number = random.randint(-100000000, 100000000)

divisors = []
for i in range(len(primes)):
    if number % primes[i] == 0:
        divisors.append(primes[i])

print("Простите делители на", number, "между 1 и 20 са", divisors)
