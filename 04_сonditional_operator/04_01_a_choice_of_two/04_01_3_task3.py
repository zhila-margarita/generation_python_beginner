# Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.
a = int(input())
b = int(input())
c = int(input())
res = 0
if a % 2 == 0:
    res = res + 1
if b % 2 == 0:
    res = res + 1
if c % 2 == 0:
    res = res + 1
print("количество четных чисел — ", res)
