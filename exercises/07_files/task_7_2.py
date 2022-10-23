# -*- coding: utf-8 -*-
"""
Завдання 7.2

Створити скрипт, який оброблятиме конфігураційний файл комутатора і виводити на
екран рядки з конфіга, крім деяких.

Ім'я конфігураційного файлу передається як аргумент скрипту:
$ python task_7_2.py config_sw1.txt

Вивести на стандартний потік виведення команди з переданого конфігураційного
файлу, крім рядків, які починаються з '!'.

Вивід має бути без порожніх рядків.

Приклад роботи завдання:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""
