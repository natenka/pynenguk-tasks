# -*- coding: utf-8 -*-
"""
Завдання 5.1

Запросити користувача введення індексу (числа). Вивести слово зі списку words,
яке відповідає введеному індексу, але у нижньому регістрі.

Приклад виконання скрипту:
$ python task_5_1.py
Enter separator: 0
guido

$ python task_5_1.py
Enter separator: 5
on

$ python task_5_1.py
Enter separator: 6
python

У цьому завданні вважаємо, що користувач завжди вводить правильний індекс.
Тобто на цьому етапі не потрібно враховувати ситуацію, коли виникає виняток
IndexError.

Обмеження: не можна редагувати список words.
"""
words = [
    'Guido', 'van', 'Rossum', 'began', 'working', 'on',
    'Python', 'in', 'the', 'late', '1980s',
]

index = int(input("Enter separator: "))
print(words[index].lower())
