"""Ровно в одном 1️⃣
Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2. Функция должна возвращать значение True, если слова имеют одинаковую длину и отличаются одним символом на одной и той же позиции, или False в противном случае.

Примечание. Приведённый ниже код:

print(is_one_away('bike', 'hike'))
print(is_one_away('water', 'wafer'))
print(is_one_away('abcd', 'abpo'))
print(is_one_away('abcd', 'abcde'))


должен выводить:

True
True
False
False"""


# объявление функции
def is_one_away(word1, word2):
    # Если длины разные, сразу выходим
    if len(word1) != len(word2):
        return False
    
    cnt = 0 # счетчик отличий
    for i in range(len(word1)):
        # Если буквы на одной позиции не совпали
        if word1[i] != word2[i]:
            cnt += 1
        # Если отличий уже больше одного, дальше не ищем
        if cnt > 1:
            return False
            
    # Возвращаем True, только если отличие было ровно одно
    return cnt == 1

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию и печатаем результат
print(is_one_away(txt1, txt2))
