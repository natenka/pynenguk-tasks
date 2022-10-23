# -*- coding: utf-8 -*-
"""
Завдання 6.5

Функція randint(1, 9) при кожному виклику повертає випадкове число діапазону
від 1 до 9 (включаючи 1 і 9). Спробуйте запустити код завдання кілька разів,
значення random_number змінюватиметься.

У цьому завданні пишемо гру з вгадування числа. За допомогою randint отримуємо
випадкове число random_number від 1 до 9 (ця частина зроблена). Потім треба
дати користувачеві 5 спроб на те, щоб вгадати це значення.

На кожній спробі потрібно запитати у користувача введення числа в діапазоні від
1 до 9. Якщо значення, що введене користувачем, дорівнює random_number, вивести
на екран повідомлення "Correct!" та зупинити гру.

Якщо введене користувачем значення не дорівнює random_number:
* якщо random_number більше за введене значення, вивести на екран повідомлення
  "Your guess is too low"
* якщо random_number менше за введене значення, вивести на екран повідомлення
  "Your guess is too high"

Якщо після 5-ти спроб число не вгадано, вивести "Number not guessed after 5 tries".

Приклад запуску завдання для числа 3
$ python task_6_5.py
Enter number: 1
Your guess is too low
Enter number: 6
Your guess is too high
Enter number: 2
Your guess is too low
Enter number: 5
Your guess is too high
Enter number: 4
Your guess is too high
Number not guessed after 5 tries

Приклад запуску завдання для числа 7
$ python task_6_5.py
Enter number: 6
Your guess is too low
Enter number: 9
Your guess is too high
Enter number: 8
Your guess is too high
Enter number: 7
Correct!

"""
from random import randint

random_number = randint(1, 9)
# print(random_number)
