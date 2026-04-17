'''Аве, Цезарь 🌶️
На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

Формат входных данных 
На вход программе подаётся строка текста на английском языке.

Формат выходных данных
Программа должна вывести зашифрованный текст в соответствии с условием задачи.

Примечание. Символы, не являющиеся английскими буквами, не изменяются.'''

text = input()
words = text.split(" ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
len_alphabet = 26

res_list = []

for word in words:
    # 1. Считаем чистую длину слова (только буквы)
    word_shift = 0
    for char in word:
        if char.isalpha():
            word_shift += 1
    
    encoded_word = ""
    # 2. Шифруем буквы слова
    for char in word:
        lower_char = char.lower()

        if lower_char in alphabet:
            index = alphabet.find(lower_char)
            new_index = (index + word_shift) % len_alphabet
            new_char = alphabet[new_index]

            if char.isupper():
                encoded_word += new_char.upper()
            else:
                encoded_word += new_char  
        else:
            # Символ не из алфавита — добавляем без изменений
            encoded_word += char 

    # Добавляем готовое слово в итоговый список
    res_list.append(encoded_word)

# Соединяем слова пробелом
print(" ".join(res_list))