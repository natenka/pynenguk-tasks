"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_10.py
Green
RED
Pink
YELLOW
white
Black

Потрібно змінити код таким чином, щоб під час виконання коду був такий вивід
$ python task_10.py
green
red
pink
yellow
white
black

При цьому не можна змінювати список colors.
"""
colors = ["Green", 'RED', 'Pink', 'YELLOW', 'white', 'Black']

for color in colors:
    print(color)
