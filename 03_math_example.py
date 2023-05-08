# Намиране на простите делители между 1 и 20 на дадено число
# Създаване на списък с простите числа между 1 и 20
primes = [2, 3, 5, 7, 11, 13, 17, 19]

# Въвеждане на цяло число от клавиатурата
number = int(input("Въведете цяло число:"))

divisors = []
for i in range(len(primes)):
    if number % primes[i] == 0:
        divisors.append(primes[i])

print("Простите делители между 1 и 20 са", divisors)
