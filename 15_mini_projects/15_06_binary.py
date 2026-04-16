# программа для перевода чисел в десятичное


def to_base_10(num, base):
    digits = "0123456789ABCDEF"
    reversed_num = num[::-1]
    res = 0

    for i in range(len(reversed_num)):
        char = reversed_num[i].upper()

        # Находим, на каком месте стоит символ в справочной строке и вытаскиваем индекс, равный значению цифры
   
        digit = digits.index(char)
        res += digit * (base**i)
    return res


num = input("Введите число: ")
base = int(input("Укажите исходную систему счисления (2, 10, 16): "))

print(to_base_10(num, base))
