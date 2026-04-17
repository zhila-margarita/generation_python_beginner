'''Используя списочное выражение, дополните приведённый ниже код так, чтобы получить список всех целых чисел-палиндромов от 100 до 1000 (включительно) в порядке возрастания.

Исходный код:

palindromes = 

print(palindromes)

'''

palindromes = [number for number in range (100,1001) if str(number) == str(number)[::-1]]

print(palindromes)
