# Звёздный прямоугольник
# Напишите программу, которая выводит прямоугольник, по периметру состоящий из звёздочек (*).
# Примечание. Высота и ширина прямоугольника равны 4 и 17 звёздочкам соответственно.
symbol = "*"
width = 17
firstandlast_string = symbol * width
mid = symbol + ((width-2)* " ") + symbol
print(firstandlast_string, mid, mid, firstandlast_string, sep="\n")
