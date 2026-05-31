"""Магазин канцелярских товаров
Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров. Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера. Также известно, что стоимость карандаша составляет 3 рубля. Требуется определить общую стоимость покупки.

https://stepik.org/lesson/811743/step/15?auth=login&unit=815018"""

x, y, z = map(int, input().split())

pencil_price = 3
pen_price = pencil_price + 2
marker_price = pen_price + 7

total_price = pencil_price * x + pen_price * y + marker_price * z
print(total_price)
