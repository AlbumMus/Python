# Задание 1
list_sabina = [True, None, 259, 25.69, "Сказочный лес"]
print(list_sabina)
n = 0
while n < 5:
    print(type(list_sabina[n]))
    n+= 1


# Задание 2
array = [1, 5, 3, 6, 8, 3, 9, 0, 5]

n = 0
for item in array:
    print("n = ", n)

    if (n % 2 != 0):
        temp = array[n-1]
        array[n-1] = array[n]
        array[n] = temp

    print(n, " ", array);
    n += 1

# Задание 3
# решение через list
mounth = int(input("Введите месяц в виде целого числа от 1 до 12: "))
mounth_list = ["Осень", "Зима", "Весна", "Лето"]
spring_min = 3
spring_max = 5
summer_min = 6
summer_max = 8
fall_min = 9
fall_max = 11

if spring_min <= mounth <= spring_max:
    print(mounth_list[2])
elif summer_min <= mounth <= summer_max:
    print(mounth[3])
elif fall_min <= mounth <= fall_max:
    print(mounth_list[0])
else:
    print(mounth_list[1])

# Решение через dict
mounth = int(input("Введите месяц в виде целого числа от 1 до 12: "))
mounth_dict = {
    "Осень": [9, 10, 11],
    "Зима": [12, 1, 2],
    "Весна": [3, 4, 5],
    "Лето": [6, 7, 8]
}

for key, value in mounth_dict.items():

    if (mounth in value):
        print(key)


# Задание 4
str = input("Введите предложение: ")
print(str.split(" "))

for num, item in enumerate(str.split(" ")):
    print(num, item[:10])

# Задание 5
rating = [8, 4, 4, 2, 1]
ch = int(input("Введите новый элемент рейтинга: "))

rating.insert(0, ch)

rating.sort(reverse=True)
print(rating)


