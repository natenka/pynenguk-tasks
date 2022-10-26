# -*- coding: utf-8 -*-
"""
Завдання 19.3a

Створити функцію send_command_to_devices, яка надсилає список вказаних команд
show на різні пристрої паралельних потоків, а потім записує вивід команд у
файл. Вивід з пристроїв у файлі може бути в будь-якому порядку, але
вивід команд з одного пристрою має йти по порядку. Наприклад, для словника
commands та пристрою 192.168.100.1 спочатку має бути вивід sh ip int br,
потім sh int desc.

Параметри функції:
* devices - список словників з параметрами підключення до пристроїв
* commands_dict - словник у якому зазначено на який пристрій надсилати якісь
  команди. Приклад словника - commands
* filename - ім'я файлу, до якого будуть записані виводи всіх команд
* limit – максимальна кількість паралельних потоків (за замовчуванням 3)

Функція нічого не повертає.

Вивід команд має бути записано у файл у такому форматі (перед вивідом кожної
команди треба написати ім'я хоста та саму команду):

R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          87   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R1#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.30.0.1               -   aabb.cc00.6530  ARPA   Ethernet0/3.300
Internet  10.100.0.1              -   aabb.cc00.6530  ARPA   Ethernet0/3.100
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down
R3#sh ip route | ex -

Gateway of last resort is not set

      10.0.0.0/8 is variably subnetted, 4 subnets, 2 masks
O        10.1.1.1/32 [110/11] via 192.168.100.1, 07:12:03, Ethernet0/0
O        10.30.0.0/24 [110/20] via 192.168.100.1, 07:12:03, Ethernet0/0

Для виконання завдання можна створювати будь-які додаткові функції, а також
використовувати функції, створені в попередніх завданнях.

Перевірити роботу функції на пристроях із файлу devices.yaml.

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""

commands = {
    "192.168.100.3": ["sh ip int br", "sh ip route | ex -"],
    "192.168.100.1": ["sh ip int br", "sh int desc"],
    "192.168.100.2": ["sh int desc"],
}
