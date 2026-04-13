"""Генератор безопасных паролей
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

Составляющие проекта:

Целые числа (тип int);
Переменные;
Ввод / вывод данных (функции input() и print());
Условный оператор (if/elif/else);
Цикл for;
Написание пользовательских функций;
Работа с модулем random для генерации случайных чисел.

Заголовок программы
Подключите модуль random;
Создайте строковые константы:
digits: 0123456789;
lowercase_letters: abcdefghijklmnopqrstuvwxyz;
uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
punctuation: !#$%&*+-=?@^_.
Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.

Считывание пользовательских данных
Программа должна запрашивать у пользователя следующую информацию:

Количество паролей для генерации;
Длину одного пароля;
Включать ли цифры 0123456789?
Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
Включать ли символы !#$%&*+-=?@^_?
Исключать ли неоднозначные символы il1Lo0O?

Настройка генерируемых паролей
На основании введенной пользователем информации, сформируйте переменную chars, содержащую все символы, которые могут быть в генерируемом пароле.
"""

import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."
chars = ''

# 1. ОПРЕДЕЛЯЕМ ФУНКЦИЮ
def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

# 2. ЗАПРОС ДАННЫХ
quantity = int(input("Количество паролей для генерации: "))
length = int(input("Длину одного пароля: "))

has_digits = input(f"Включать ли цифры {digits}? (да/нет): ").lower()
has_uppercase = input(f"Включать ли прописные буквы {uppercase_letters}? (да/нет): ").lower()
has_lowercase = input(f"Включать ли строчные буквы {lowercase_letters}? (да/нет): ").lower()
has_symbols = input(f"Включать ли символы {punctuation}? (да/нет): ").lower()
has_ambiguous = input("Исключать ли неоднозначные символы il1Lo0O? (да/нет): ").lower()

confirmation = ['да', 'lf']

# 3. ФОРМИРУЕМ ПУЛ СИМВОЛОВ (chars)
if has_digits in confirmation:
    chars += digits
if has_uppercase in confirmation:
    chars += uppercase_letters
if has_lowercase in confirmation:
    chars += lowercase_letters
if has_symbols in confirmation:
    chars += punctuation

if has_ambiguous in confirmation:
    for c in "il1Lo0O":
        chars = chars.replace(c, "")

# 4. ГЕНЕРАЦИЯ 
if not chars:
    print("Вы не выбрали ни одного набора символов! Не из чего генерировать.")
else:
    print("\nВаши сгенерированные пароли:")
    for _ in range(quantity):
        # Вызываем нашу функцию, передавая ей нужную длину и набор символов
        print(generate_password(length, chars))