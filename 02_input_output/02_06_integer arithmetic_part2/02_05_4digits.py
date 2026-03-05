num = int(input())
digit1 = (num // 10**3) % 10
digit2 = (num // 10**2) % 10
digit3 = (num // 10**1) % 10
digit4 = (num // 10**0) % 10
print(digit1, digit2, digit3, digit4)
print("Цифра в позиции тысяч равна", digit1)
print("Цифра в позиции сотен равна", digit2)
print("Цифра в позиции десятков равна", digit3)
print("Цифра в позиции единиц равна", digit1)