"""Змеиный регистр 🐍
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

Примечание 1. Почитать подробнее о стилях именования можно по ссылке.

Примечание 2. Приведённый ниже код:

print(convert_to_python_case('ThisIsCamelCased'))
print(convert_to_python_case('IsPrimeNumber'))


должен выводить:

this_is_camel_cased
is_prime_number"""


# объявление функции
def convert_to_python_case(text):
    res = text[0].lower()
    for char in text[1:]:
        if char.isupper():
            res += "_" + char.lower()
        else:
            res += char
    return res


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
