# -*- coding: utf-8 -*-
"""
Завдання 18.2b

Копіювати функцію send_config_commands із завдання 18.2a та додати перевірку на
помилки.

При виконанні кожної команди скрипт повинен перевіряти результат на такі
помилки: Invalid input detected, Incomplete command, Ambiguous command

Якщо під час виконання однієї з команд виникла помилка, функція повинна
виводити повідомлення на стандартний потік виведення з інформацією про те, яка
помилка виникла, при виконанні якої команди та на якому пристрої, наприклад:
The command "logging" failed with the error "Incomplete command." on device 192.168.100.1

Помилки повинні виводитися завжди незалежно від значення параметра log. При
цьому параметр log, як і раніше, повинен контролювати, чи буде виводитися
повідомлення:
Connecting to 192.168.100.1...

Функція send_config_commands тепер має повертати кортеж із двох словників:
* перший словник із виведенням команд, які виконалися без помилки
* другий словник із виведенням команд, які виконалися з помилками

Обидва словники у форматі (приклади словників нижче):
* ключ - команда
* значення - вивід із виконанням команд

Перевірити роботу функції можна на одному пристрої.

Приклад роботи функції send_config_commands:

In [16]: commands
Out[16]:
['logging 0255.255.1',
 'logging',
 'a',
 'logging buffered 20010',
 'ip http server']

In [17]: result = send_config_commands(r1, commands)
connecting to 192.168.100.1...
The command "logging 0255.255.1" failed with the error "Invalid input detected at '^' marker." on device 192.168.100.1
The command "logging" failed with the error "Incomplete command." on device 192.168.100.1
The command "a" failed with the error "Ambiguous command:  "a"" on device 192.168.100.1

In [18]: pprint(result, width=120)
({'ip http server': 'config term\n'
                    'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                    'R1(config)#ip http server\n'
                    'R1(config)#',
  'logging buffered 20010': 'config term\n'
                            'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                            'R1(config)#logging buffered 20010\n'
                            'R1(config)#'},
 {'a': 'config term\n'
       'Enter configuration commands, one per line.  End with CNTL/Z.\n'
       'R1(config)#a\n'
       '% Ambiguous command:  "a"\n'
       'R1(config)#',
  'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

In [19]: good, bad = result

In [20]: good.keys()
Out[20]: dict_keys(['logging buffered 20010', 'ip http server'])

In [21]: bad.keys()
Out[21]: dict_keys(['logging 0255.255.1', 'logging', 'a'])


Приклади команд з помилками:
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]

commands = commands_with_errors + correct_commands
