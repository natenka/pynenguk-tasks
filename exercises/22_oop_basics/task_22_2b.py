# -*- coding: utf-8 -*-

"""
Завдання 22.2b

Копіювати клас CiscoTelnet із завдання 22.2a та додати метод send_config_commands.

Метод send_config_commands повинен вміти надсилати одну команду
конфігураційного режиму та список команд. Метод повинен повертати вивід
аналогічний методу send_config_set у Netmiko (приклад виведення нижче).

Приклад створення екземпляра класу:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'host': '192.168.139.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Використання методу send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

"""
