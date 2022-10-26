# -*- coding: utf-8 -*-
"""
Завдання 18.3

Створити функцію send_commands (для підключення SSH використовується netmiko).

Параметри функції:
* device - словник із параметрами підключення до одного пристрою
* show - одна команда show (рядок)
* config - список із командами, які треба виконати в конфігураційному режимі

Аргументи show та config мають передаватися лише як ключові. При передачі цих
аргументів як позиційних, має генеруватися виняток TypeError.

In [4]: send_commands(r1, 'sh clock')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-75adcfb4a005> in <module>
----> 1 send_commands(r1, 'sh clock')

TypeError: send_commands() takes 1 positional argument but 2 were given

Залежно від того, який аргумент було передано, функція викликає різні функції
всередині. При виклику функції send_commands завжди повинен передаватися лише
один з аргументів show, config. Якщо передаються обидва аргументи, має
генеруватися виняток ValueError.

Далі комбінація з аргументу та відповідної функції:
* show - функція send_show_command із завдання 18.1
* config - функція send_config_commands із завдання 18.2

Функція повертає рядок із результатами виконання команд чи команди.

Перевірити роботу функції:
* зі списком команд commands
* командою command

Приклад роботи функції:

In [14]: send_commands(r1, show='sh clock')
Out[14]: '*17:06:12.278 UTC Wed Mar 13 2019'

In [15]: commands = ['username user5 password pass5', 'username user6 password pass6']

In [16]: send_commands(r1, config=commands)
Out[16]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#username user5 password pass5\nR1(config)#username user6 password pass6\nR1(config)#end\nR1#'

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"
