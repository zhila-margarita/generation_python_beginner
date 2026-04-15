"""Дешифр брутфорсом"""

# Дешифр брутфорсом
# Поддержка: русский (без ё), английский


# 1. Ввод и проверка данных

while True:
    language = input("Выберите язык: rus или eng: ").lower()
    if language in ["rus", "eng"]:
        break
    print("Ошибка! Используйте 'rus' или 'eng' (без кавычек).")


text = input("Введите текст для обработки: ")


# 2. Настройка алфавита
if language == "rus":
    alphabet = "".join([chr(i) for i in range(ord("а"), ord("я") + 1)])  # 32 буквы
    shift_range = 32

elif language == "eng":
    alphabet = "".join([chr(i) for i in range(ord("a"), ord("z") + 1)])  # 26 букв
    shift_range = 26
len_alphabet = len(alphabet)


# 3. Основной цикл
for current_shift in range(shift_range):
    res = ""
    # Для дешифрования сдвигаем назад
    actual_shift = -current_shift

    for char in text:
        lower_char = char.lower()
        if lower_char in alphabet:
            index = alphabet.find(lower_char)
            new_index = (index + actual_shift) % len_alphabet
            new_char = alphabet[new_index]
            res += new_char.upper() if char.isupper() else new_char
        else:
            res += char

    print(f"Сдвиг {current_shift}: {res}")
