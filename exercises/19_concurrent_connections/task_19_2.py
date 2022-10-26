# -*- coding: utf-8 -*-
"""
Завдання 19.2

Створити функцію send_show_command_to_devices, яка відправляє однакову команду
show на різні пристрої в паралельних потоках, а потім записує вивід команд
у файл. Вивід із пристроїв у файлі може бути у будь-якому порядку.

Параметри функції:
* devices - список словників з параметрами підключення до пристроїв
* command - команда
* filename - ім'я текстового файлу, до якого будуть записані виводи всіх команд
* limit – максимальна кількість паралельних потоків (за замовчуванням 3)

Функція нічого не повертає.

Підключення до обладнання виконується за допомогою Netmiko (SSH).

Вивід команд має бути записано у звичайний текстовий файл у такому форматі
(перед вивідом команди треба написати ім'я хоста і саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для виконання завдання можна створювати додаткові функції.

Перевірити роботу функції на пристроях із файлу devices.yaml.

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""
