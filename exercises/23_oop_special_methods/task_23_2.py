# -*- coding: utf-8 -*-

"""
Завдання 23.2

Копіювати клас CiscoTelnet із завдання 22.2 та додати класу підтримку роботи в
менеджері контексту. При виході з блоку менеджера контексту має закриватися
з'єднання.

Приклад роботи:

In [14]: r1_params = {
    ...:     'ip': '192.168.139.1',
    ...:     'username': 'cisco',
    ...:     'password': 'cisco',
    ...:     'secret': 'cisco'}

In [15]: from task_23_2 import CiscoTelnet

In [16]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:
sh clock
*19:17:20.244 UTC Sat Apr 6 2019
R1#

In [17]: with CiscoTelnet(**r1_params) as r1:
    ...:     print(r1.send_show_command('sh clock'))
    ...:     raise ValueError('Виникла помилка')
    ...:
sh clock
*19:17:38.828 UTC Sat Apr 6 2019
R1#
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-f3141be7c129> in <module>
      1 with CiscoTelnet(**r1_params) as r1:
      2     print(r1.send_show_command('sh clock'))
----> 3     raise ValueError('Виникла помилка')
      4

ValueError: Виникла помилка

Тест перевіряє підключення до параметрів з файлу devices.yaml. Там мають бути
вказані доступні пристрої.
"""
