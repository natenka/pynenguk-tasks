# -*- coding: utf-8 -*-
"""
Завдання 21.5

Створити функцію send_and_parse_command_parallel.

Функція send_and_parse_command_parallel повинна запускати у паралельних потоках
функцію send_and_parse_show_command із завдання 21.4.

Параметри функції send_and_parse_command_parallel:

* devices - список словників з параметрами підключення до пристроїв
* command - команда
* templates_path - шлях до каталогу із шаблонами TextFSM
* limit – максимальна кількість паралельних потоків (за замовчуванням 3)

Функція повинна повертати словник:

* ключі - IP-адреса пристрою з якого отримано вивід
* значення - список словників (вивід, який повертає функція send_and_parse_show_command)

Приклад словника:
{'192.168.100.1': [{'intf': 'Ethernet0/0',
                    'address': '192.168.100.1',
                    'status': 'up',
                    'protocol': 'up'},
                   {'intf': 'Ethernet0/1',
                    'address': '192.168.200.1',
                    'status': 'up',
                    'protocol': 'up'}],
 '192.168.100.2': [{'intf': 'Ethernet0/0',
                    'address': '192.168.100.2',
                    'status': 'up',
                    'protocol': 'up'},
                   {'intf': 'Ethernet0/1',
                    'address': '10.100.23.2',
                    'status': 'up',
                    'protocol': 'up'}]}

Перевірити роботу функції на прикладі виведення команди sh ip int br та
пристроях з devices.yaml.
"""
