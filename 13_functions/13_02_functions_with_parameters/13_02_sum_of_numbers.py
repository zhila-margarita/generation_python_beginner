"""Сумма цифр
Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.
"""


# объявление функции
def print_digit_sum(num):
    res = 0
    for el in str(num):
        res = int(el) + res
    print(res)


# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
