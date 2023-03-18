# -*- coding: utf-8 -*-
"""
Завдання 25.2

Для завдань 25 розділу немає тестів!

У цьому завданні необхідно створити скрипт get_data.py.

Код у скриптах має бути розбитий на функції.  Які саме функції та як розділити
код, треба вирішити самостійно.  Частина коду може бути глобальною.

Скрипт можуть передаватися аргументи і, залежно від аргументів, треба виводити
різну інформацію.  Якщо скрипт викликаний:
* без аргументів, вивести весь вміст таблиці dhcp
* з двома аргументами, вивести інформацію з таблиці dhcp, яка відповідає полю
  та значенню
* з будь-якою іншою кількістю аргументів, вивести повідомлення, що скрипт
  підтримує тільки два або нуль аргументів

Файл БД можна скопіювати із завдання 25.1.
Приклади роботи коду для різної кількості та значень аргументів:

$ python get_data.py

The dhcp table has the following entries:
-----------------  ---------------  --  ----------------  ---
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2
-----------------  ---------------  --  ----------------  ---

$ python get_data.py vlan 10

Information about devices with the following parameters: vlan 10
-----------------  ----------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2
-----------------  ----------  --  ---------------  ---

$ python get_data.py ip 10.1.10.2

Information about devices with the following parameters: ip 10.1.10.2
-----------------  ---------  --  ---------------  ---
00:09:BB:3D:D6:58  10.1.10.2  10  FastEthernet0/1  sw1
-----------------  ---------  --  ---------------  ---

$ python get_data.py vln 10
This parameter is not supported.
Valid parameter values: mac, ip, vlan, interface, switch

$ python get_data.py ip vlan 10

Please enter two or zero arguments
"""
