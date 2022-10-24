# -*- coding: utf-8 -*-
"""
Завдання 15.4

Створити функцію get_ints_without_description, яка очікує як аргумент на ім'я
файлу, в якому знаходиться конфігурація пристрою.

Функція повинна обробляти конфігурацію та повертати список імен інтерфейсів, на
яких немає опису (команди description).

Приклад підсумкового списку:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Приклад інтерфейсу з описом:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0

Інтерфейс без опису:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Перевірити функцію на прикладі файлу config_r1.txt.

Приклад виклику функції
In [15]: get_ints_without_description("config_r1.txt")
Out[15]: ['Loopback0', 'Tunnel0', 'Ethernet0/1', 'Ethernet0/3.100', 'Ethernet1/0']

"""
