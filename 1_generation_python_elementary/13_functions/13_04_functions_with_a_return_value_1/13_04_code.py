'''</code>
Напишите функцию code_format(text), которая принимает строку текста text, оборачивает её в теги <code></code> и возвращает результат.

Примечание 1. Приведённый ниже код:

print(code_format('s = input()'))
print(code_format('15'))
print(code_format('None'))

                  
должен выводить:

<code>s = input()</code>
<code>15</code>
<code>None</code>

                  
Примечание 2. Во многих тестовых задачах мы обёртываем варианты ответа именно в теги <code></code>.'''

# объявление функции
def code_format(text):
    return "<code>"+text+"</code>"

# считываем данные
text = input()

# вызываем функцию
print(code_format(text))