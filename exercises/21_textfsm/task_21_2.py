# -*- coding: utf-8 -*-
"""
Завдання 21.2

Зробити шаблон TextFSM для обробки виводу sh ip dhcp snooping binding та
записати його у файл templates/sh_ip_dhcp_snooping.template

Вивід команди знаходиться у файлі output/sh_ip_dhcp_snooping.txt.

Шаблон повинен обробляти та повертати значення таких стовпців:

* mac - такого виду 00:04:A3:3E:5B:69
* ip - такого виду 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Перевірити роботу шаблону за допомогою функції parse_command_output із завдання 21.1.
"""
