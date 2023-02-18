# -*- coding: utf-8 -*-
"""
Завдання 18.2c

Копіювати функцію send_config_commands із завдання 18.2b та переробити її таким
чином:
Якщо під час виконання команди виникла помилка, запитати користувача треба
виконувати інші команди.

Варіанти відповіді [y]/n:
* y - виконувати решту команд. Це значення за промовчанням, тому натискання
  будь-якої комбінації сприймається як y
* n чи no - не виконувати інші команди

Функція send_config_commands, як і раніше, повинна повертати кортеж із двох
словників:
* перший словник із виведенням команд, які виконалися без помилки
* другий словник із виведенням команд, які виконалися з помилками

Обидва словники у форматі
* ключ - команда
* значення - вивід із виконанням команд

Перевірити роботу функції можна на одному пристрої.
Приклад роботи функції:

In [11]: result = send_config_commands(r1, commands)
Connecting to 192.168.100.1...
The command "logging 0255.255.1" failed with the error "Invalid input detected at '^' marker." on device 192.168.100.1
Continue executing commands? [y]/n: y
The command "logging" failed with the error "Incomplete command." on device 192.168.100.1
Continue executing commands? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})


У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands
