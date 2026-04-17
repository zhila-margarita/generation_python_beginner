# Три города 🏙️
# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Формат входных данных: на вход программе подаются названия трёх городов, каждое на отдельной строке.
# Формат выходных данных: программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

# Примечание. Гарантируется, что длины названий всех трёх городов различны.

city_1, city_2, city_3 = input(), input(), input()
max_length = max(len(city_1), len(city_2), len(city_3))
min_length  = min(len(city_1), len(city_2), len(city_3))
if max_length == len (city_1):
    maximum = city_1
elif max_length == len (city_2):
    maximum = city_2
else:
    maximum = city_3
if min_length == len (city_1):
    minimum = city_1
elif min_length == len (city_2):
    minimum = city_2
else:
    minimum = city_3
print (minimum, maximum, sep = "\n")