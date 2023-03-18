# -*- coding: utf-8 -*-

"""
Завдання 22.2a

Копіювати клас CiscoTelnet із завдання 22.2 та змінити метод send_show_command
додавши три параметри:

* parse - контролює те, чи повертатиметься звичайний вивід команди або
  список словників, отриманий після обробки за допомогою TextFSM.
  * parse=True - повинен повертатися список словників
  * parse=False - звичайний вивід. Значення за замовчуванням - True
* templates - шлях до каталогу із шаблонами. Значення за замовчуванням - "templates"
* index - ім'я файлу, де зберігається відповідність між командами та шаблонами.
  Значення за замовчуванням - "index"


Приклад створення екземпляра класу:

In [1]: r1_params = {
   ...:     'host': '192.168.139.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_22_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Використання методу send_show_command:
In [4]: r1.send_show_command("sh host int br", parse=True)
Out[4]:
[{'address': '192.168.139.1',
  'intf': 'Ethernet0/0',
  'status': 'up',
  'protocol': 'up'},
 {'address': '192.168.200.1',
  'intf': 'Ethernet0/1',
  'status': 'up',
  'protocol': 'up'},
 {'address': '192.168.130.1',
  'intf': 'Ethernet0/2',
  'status': 'up',
  'protocol': 'up'}]

In [5]: r1.send_show_command("sh host int br", parse=False)
Out[5]: 'sh host int br\r\nInterface                  host-Address      OK? Method Status
Protocol\r\nEthernet0/0                192.168.139.1   YES NVRAM  up
up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up...'

"""
