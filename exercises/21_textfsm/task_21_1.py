# -*- coding: utf-8 -*-
"""
Завдання 21.1

Створити функцію parse_command_output. Параметри функції:

* template - ім'я файлу, в якому знаходиться шаблон TextFSM Наприклад,
  templates/sh_ip_int_br.template
* command_output - виведення відповідної команди show (рядок)

Функція повинна повертати список:

* перший елемент - це список із назвами стовпців
* решта елементів це списки, в якому знаходяться результати обробки виводу


Перевірити роботу функції на виведенні команди sh ip int br з обладнання та
шаблон templates/sh_ip_int_br.template.

Приклад роботи функції

In [5]: with open("output/sh_ip_int_br.txt") as f:
   ...:     output = f.read()
   ...: result = parse_command_output("templates/sh_ip_int_br.template", output)
   ...: pprint(result)
   ...:
[['intf', 'address', 'status', 'protocol'],
 ['FastEthernet0/0', '15.0.15.1', 'up', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'up', 'up'],
 ['FastEthernet0/3', 'unassigned', 'up', 'up'],
 ['Loopback0', '10.1.1.1', 'up', 'up'],
 ['Loopback100', '100.0.0.1', 'up', 'up']]

"""
from netmiko import Netmiko


# виклик функції має виглядати так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.139.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with Netmiko(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
