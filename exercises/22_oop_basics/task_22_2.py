# -*- coding: utf-8 -*-

"""
Завдання 22.2

Створити клас CiscoTelnet, який підключається по Telnet до обладнання Cisco.

Під час створення екземпляра класу, має створюватися підключення Telnet, і
перехід у режим enable. Клас повинен використовувати модуль telnetlib для
підключення Telnet.

У класу CiscoTelnet, крім __init__, має бути, як мінімум, два методи:

* _write_line - приймає як аргумент рядок і відправляє на обладнання рядок
  перетворений на байти і додає переклад рядка в кінці. Метод _write_line має
  використовуватись усередині класу.
* send_show_command - приймає як аргумент команду show і повертає вивід,
  отриманий з обладнання
* close - закриває сесію Telnet

Параметри методу init:

* ip - IP-адреса
* username - ім'я користувача
* password - пароль
* secret - пароль enable

Приклад створення екземпляра класу:

In [2]: from task_22_2 import CiscoTelnet

In [3]: r1_params = {
   ...:     'host': '192.168.139.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}
   ...:

In [4]: r1 = CiscoTelnet(**r1_params)

In [5]: r1.send_show_command("sh ip int br")
Out[5]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.139.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                unassigned      YES manual up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nR1#'


Підказка:
Метод _write_line потрібен для того, щоб можна було скоротити рядок:
self.telnet.write(line.encode("ascii") + b"\n")

до такого:
self._write_line(line)

Він не повинен робити нічого іншого.
"""
