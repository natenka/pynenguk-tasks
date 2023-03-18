# -*- coding: utf-8 -*-

"""
Завдання 24.2d

Скопіювати клас MyNetmiko із завдання 24.2c або завдання 24.2b.

Додати параметр ignore_errors до методу send_config_set. Якщо передано
ignore_errors=True, не треба виконувати перевірку на помилки і метод повинен
працювати так само, як метод send_config_set в netmiko. Якщо
ignore_errors=False, помилки повинні перевірятися.

За замовчуванням помилки повинні ігноруватися.

In [2]: from task_24_2d import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [6]: r1.send_config_set('lo')
Out[6]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [7]: r1.send_config_set('lo', ignore_errors=True)
Out[7]: 'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\nR1(config)#lo\n% Incomplete command.\n\nR1(config)#end\nR1#'

In [8]: r1.send_config_set('lo', ignore_errors=False)
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-8-704f2e8d1886> in <module>()
----> 1 r1.send_config_set('lo', ignore_errors=False)

...
ErrorInCommand: When executing the command "lo" on device 192.168.139.1 an error occurred "Incomplete command."

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до пристроїв відрізняються, потрібно
змінити параметри у файлі devices.yaml.
"""
