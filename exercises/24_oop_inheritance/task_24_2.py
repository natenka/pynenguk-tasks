# -*- coding: utf-8 -*-

"""
Завдання 24.2

Створити клас MyNetmiko, який успадковує клас CiscoIosSSH з Netmiko.

Переписати метод __init__ у класі MyNetmiko таким чином, щоб після підключення SSH
виконувався перехід у режим enable.

Для цього в методі __init__ повинен спочатку викликатися метод __init__ класу
CiscoIosSSH, а потім зроблений перехід в режим enable.

Перевірити, що в MyNetmiko класі доступні методи send_command і send_config_set
(вони успадковуються автоматично, це тільки для перевірки).

In [2]: from task_24_2 import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.139.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.139            10.139.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '


У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до пристроїв відрізняються, потрібно
змінити параметри у файлі devices.yaml.
"""
from netmiko.cisco.cisco_ios import CiscoIosSSH


device_params = {
    "device_type": "cisco_ios",
    "host": "192.168.139.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}
