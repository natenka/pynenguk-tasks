# -*- coding: utf-8 -*-

"""
Завдання 24.2b

Копіювати клас MyNetmiko із завдання 24.2a.

Доповнити функціонал методу send_config_set netmiko та додати до нього
перевірку на помилки за допомогою методу _check_error_in_command.

Метод send_config_set повинен надсилати команди по одній та перевіряти кожну на
помилки. Якщо під час виконання команд не виявлено помилки, метод
send_config_set повертає вивід команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: When executing the command "lo" on device 192.168.139.1 an error occurred "Incomplete command."


У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до пристроїв відрізняються, потрібно
змінити параметри у файлі devices.yaml.
"""
