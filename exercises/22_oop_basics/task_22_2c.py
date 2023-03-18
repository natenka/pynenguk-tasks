# -*- coding: utf-8 -*-

"""
Завдання 22.2c

Копіювати клас CiscoTelnet із завдання 22.2b та змінити метод
send_config_commands, додавши перевірку команд на помилки.

Метод send_config_commands повинен мати додатковий параметр strict:

* strict=True означає, що при виявленні помилки, необхідно згенерувати виняток
  ValueError (значення за замовчуванням)
* strict=False означає, що при виявленні помилки, треба тільки вивести на
  стандартний потік повідомлення про помилку

Метод повинен повертати вивід аналогічний методу send_config_set у netmiko
(приклад виведення нижче). Текст виключення та помилки у прикладі нижче.

Приклад створення екземпляра класу:
In [1]: from task_22_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'host': '192.168.139.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Використання методу send_config_commands:

In [7]: print(r1.send_config_commands(commands, strict=False))
When executing the command "logging 0255.255.1" on device 192.168.139.1 an error occurred -> Invalid input detected at '^' marker.
When executing the command "logging" on device 192.168.139.1 an error occurred -> Incomplete command.
When executing the command "a" on device 192.168.139.1 an error occurred -> Ambiguous command:  "a"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#a
% Ambiguous command:  "a"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: When executing the command "logging 0255.255.1" on device 192.168.139.1 an error occurred -> Invalid input detected at '^' marker.

"""
