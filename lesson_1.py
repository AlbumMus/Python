sabina = "pretty woomen"
if sabina == "pretty woomen":
    print("она такая хорошенькая!")
else:
    print("ну просто чудовище какое-то!")


sabina = "animal"
if sabina != "pretty woomen":
    print("она такая хорошенькая!")
elif sabina == "animal":
    print("Не мышонок, не лягушка, а неведома зверушка!")
else:
    print("ну просто чудовище какое-то!")


# Задание 2
a = 240
sec = a
min = a / 60
hour = a / 3600
print(f"{hour}:{min}:{sec}")


#  Задание 3
n = input("Введите любое целое число: ")
n1 = n
n2 = n + n
n3 = n + n + n
sum = int(n1) + int(n2) + int(n3)
print(f"{n1} + {n2} + {n3} = {sum}")

# Задание 4
number_x = input("Введите любое целое число: ")
number_x = str(number_x)
n = 0
max = 0
while n < len(number_x):
    if (int(number_x[n]) > max):
        max = int(number_x[n])
    print("ch: ", number_x[n], " max: ", max)
    n += 1
print("максимальное число = ", max)


# Задание 5
a = int(input("Введите значение Выручки: "))
b = int(input("Введите значение Издержек: "))
if a > b:
    print("Вы молодцы! Работаете с прибылью!")
    p = a - b
    rent = p / a
    print(f"Рентабельность составляет: {rent}")
    sum = int(input("Введите количество сотрудников в компании: "))
    c = a / sum
    print(f"Прибыль фирмы в расчёте на одного сотрудника составит: {c}")
else:
    print("Внимание! Компания терпит убытки!")


# Задание 6
start_running = 4
end_running = 10
day = 1
while start_running < end_running:
    start_running = start_running + start_running * 0.1
    day += 1
    print(f"день: {day}")
    print(f"a = {start_running}")