# -*- coding: utf-8 -*-

"""
Завдання 24.1a

Копіювати та доповнити клас CiscoSSH із завдання 24.1.

Перед підключенням по SSH необхідно перевірити, чи у словнику з параметрами
підключення присутні такі параметри: username, password, secret. Якщо якийсь
параметр відсутній, запитати значення у користувача, а потім виконати
підключення. Якщо всі параметри присутні, виконайте підключення.

In [1]: from task_24_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'host': '192.168.139.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Enter username: cisco
Enter password: cisco
Enter enable password: cisco

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.139.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.139            10.139.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до пристроїв відрізняються, потрібно
змінити параметри у файлі devices.yaml.
"""

device_params = {"device_type": "cisco_ios", "host": "192.168.139.1"}
