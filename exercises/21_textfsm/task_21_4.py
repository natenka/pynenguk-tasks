# -*- coding: utf-8 -*-
"""
Завдання 21.4

Створити функцію send_and_parse_show_command.

Параметри функції:

* device_dict - словник із параметрами підключення до одного пристрою
* command – команда, яку треба виконати
* templates_path - шлях до каталогу із шаблонами TextFSM
* index - ім'я індекс файлу, значення за замовчуванням "index"

Функція повинна підключатися до одного пристрою, відправляти команду show за
допомогою Netmiko, а потім парсити вивід команди за допомогою TextFSM.

Функція повинна повертати список словників із результатами обробки виводу
команди (як у завданні 21.1a):

* ключі - імена змінних у шаблоні TextFSM
* значення - частини виводу, які відповідають змінним

Перевірити роботу функції на прикладі вивід команди sh ip int br та пристроях з devices.yaml.

Приклад роботи функції:
In [17]: result = send_and_parse_show_command(
    ...:     devices[1], "sh ip int br", templates_path=full_pth
    ...: )
    ...: pprint(result, width=120, sort_dicts=False)
    ...:
[{'intf': 'Ethernet0/0', 'address': '192.168.100.2', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Ethernet0/1', 'address': '10.100.23.2', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Ethernet0/2', 'address': 'unassigned', 'status': 'administratively down', 'protocol': 'down'},
 {'intf': 'Ethernet0/3', 'address': 'unassigned', 'status': 'administratively down', 'protocol': 'down'},
 {'intf': 'Loopback0', 'address': '10.2.2.2', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback9', 'address': 'unassigned', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback19', 'address': 'unassigned', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback100', 'address': '10.100.100.2', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Tunnel2', 'address': '10.255.1.2', 'status': 'up', 'protocol': 'down'}]

"""
