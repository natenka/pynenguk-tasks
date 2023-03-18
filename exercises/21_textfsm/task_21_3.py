# -*- coding: utf-8 -*-
"""
Завдання 21.3

Створити функцію parse_command_dynamic.

Параметри функції:

* command_output - вивід команди (рядок)
* attributes_dict - словник атрибутів, у якому знаходяться такі пари ключ-значення:
  * 'Command': команда
  * 'Vendor': вендор
* index_file - ім'я файлу, де зберігається відповідність між командами та
  шаблонами. Значення за замовчуванням - "index"
* templ_path – каталог, де зберігаються шаблони. Значення за замовчуванням - "templates"

Функція повинна повертати список словників із результатами обробки виводу
команди (як у завданні 21.1a):

* ключі - імена змінних у шаблоні TextFSM
* значення - частини виводу, які відповідають змінним

Перевірити роботу функції з виведенням команди sh ip int br і sh version.

Приклад виклику функції sh ip int br

In [8]: attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}
   ...: with open("output/sh_ip_int_br.txt") as f:
   ...:     output = f.read()
   ...: result = parse_command_dynamic(output, attributes)
   ...: pprint(result, width=120, sort_dicts=False)
   ...:
[{'intf': 'FastEthernet0/0', 'address': '15.0.15.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/1', 'address': '10.0.12.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/2', 'address': '10.0.13.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'FastEthernet0/3', 'address': 'unassigned', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback0', 'address': '10.1.1.1', 'status': 'up', 'protocol': 'up'},
 {'intf': 'Loopback100', 'address': '100.0.0.1', 'status': 'up', 'protocol': 'up'}]

Приклад виклику функції з sh version

In [9]: attributes = {'Command': 'sh version', 'Vendor': 'cisco_ios'}
   ...: with open("output/sh_version.txt") as f:
   ...:     output = f.read()
   ...: print(parse_command_dynamic(output, attributes))

[{'version': '15.3(2)S1', 'hostname': 'R1_LONDON'}]

"""
