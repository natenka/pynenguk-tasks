"""
Так як це перше завдання, де потрібно запитати щось у користувача, ця частина
вже написана:

number_as_str = input("Enter a number greater than 10: ")

input очікує введення користувача і після натискання enter те, що користувач
написав, потрапляє до змінної number_as_str. При цьому input завжди повертає
рядок. Тому далі рядок number_as_str ми перетворюємо на integer функцією int.

У завданні додано вивід pprint, щоб переглянути значення змінних number_as_str,
number. Використовується саме pprint, тому що звичайний print виводить на екран
у однаковому вигляді рядок "4" та число 4.

Тепер треба написати умову, яка перевірятиме значення змінної number і буде
виводити текст "correct", якщо number більше 10, та "wrong" якщо менше або
дорівнює 10.

Приклад роботи завдання
$ python task_06.py
Enter a number greater than 10: 4
'4'
4
wrong

$ python task_06.py
Enter a number greater than 10: 20
'20'
20
correct
"""

from pprint import pprint


number_as_str = input("Enter a number greater than 10: ")
number = int(number_as_str)
pprint(number_as_str)
pprint(number)
