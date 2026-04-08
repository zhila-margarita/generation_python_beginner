"""Next Prime 🌶️
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число, большее числа num.

Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

Примечание 2. Приведённый ниже код:

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))


должен выводить:

7
11
17
"""


# объявление функции
def is_prime(num):
    if num <= 1:
        return False
    # Проверяем делители от 2 до корня из num (включительно)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# объявление функции
def get_next_prime(num):
    check_num = num + 1
    # Просто крутим цикл, пока is_prime не вернет True
    while not is_prime(check_num):
        check_num += 1
    return check_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
