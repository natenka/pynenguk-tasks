# -*- coding: utf-8 -*-
"""
Завдання 18.2

Створити функцію send_config_commands

Функція підключається SSH (за допомогою netmiko) до ОДНОГО пристрою і виконує
перелік команд в конфігураційному режимі на підставі переданих аргументів.

Параметри функції:
* device - словник із параметрами підключення до пристрою
* config_commands – список команд, які треба виконати

Функція повертає рядок із результатами виконання команди:

In [7]: r1
Out[7]:
{'device_type': 'cisco_ios',
 'ip': '192.168.100.1',
 'username': 'cisco',
 'password': 'cisco',
 'secret': 'cisco'}

In [8]: commands
Out[8]: ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']

In [9]: result = send_config_commands(r1, commands)

In [10]: result
Out[10]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.
         \nR1(config)#logging 10.255.255.1\nR1(config)#logging buffered 20010\n
         R1(config)#no logging console\nR1(config)#end\nR1#'

In [11]: print(result)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 10.255.255.1
R1(config)#logging buffered 20010
R1(config)#no logging console
R1(config)#end
R1#


Скрипт повинен надсилати команду command на всі пристрої з файлу devices.yaml
за допомогою функції send_config_commands.

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
