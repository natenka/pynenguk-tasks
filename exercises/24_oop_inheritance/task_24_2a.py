# -*- coding: utf-8 -*-

"""
Завдання 24.2a

Копіювати та доповнити клас MyNetmiko із завдання 24.2.

Додати метод _check_error_in_command, який перевіряє такі помилки:
* Invalid input detected, Incomplete command, Ambiguous command

Метод чекає як аргумент команду і вивід команди. Якщо у виведенні не виявлено
помилку, метод нічого не повертає. Якщо в виведенні є помилка, метод повинен
генерувати виняток ErrorInCommand з повідомленням про те, яка помилка була
виявлена, на якому пристрої і в якій команді.

Виняток ErrorInCommand створено у файлі завдання.

Переписати метод send_command netmiko, додавши до нього перевірку помилки.

In [2]: from task_24_2a import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.139.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.139            10.139.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip br')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-1c60b31812fd> in <module>()
----> 1 r1.send_command('sh ip br')
...
ErrorInCommand: When executing the command "sh ip br" on device 192.168.139.1 an error occurred "Invalid input detected at '^' marker."


У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до пристроїв відрізняються, потрібно
змінити параметри у файлі devices.yaml.
"""


class ErrorInCommand(Exception):
    """
    Виняток генерується, якщо при виконанні команди на обладнанні виникла помилка.
    """
