# -*- coding: utf-8 -*-
"""
Завдання 21.1a

Створити функцію parse_output_to_dict.

Параметри функції:

* template - ім'я файлу, у якому міститься шаблон TextFSM. Наприклад,
  templates/sh_ip_int_br.template
* command_output - вивід відповідної команди show (рядок)

Функція повинна повертати список словників:

* ключі - імена змінних у шаблоні TextFSM
* значення - частини виводу, які відповідають змінним

Перевірити роботу функції на виведенні команди output/sh_ip_int_br.txt та
шаблоні templates/sh_ip_int_br.template.


Приклад роботи функції:
In [2]: with open("output/sh_ip_int_br.txt") as f:
   ...:     output = f.read()
   ...: result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
   ...: pprint(result, width=120, sort_dicts=False)
   ...:
[{'intf': 'FastEthernet0/0', 'address': '15.0.15.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/1', 'address': '10.0.12.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/2', 'address': '10.0.13.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/3', 'address': 'unassigned', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback0', 'address': '10.1.1.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback100', 'address': '100.0.0.1', 'status': 'up', 'protocol': 'up'}]

"""
