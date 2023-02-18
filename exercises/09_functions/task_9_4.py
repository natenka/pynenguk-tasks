# -*- coding: utf-8 -*-
"""
Завдання 9.4

Створити функцію generate_access_config, яка генерує конфігурацію для портів access.

Функція повинна мати два параметри:
* intf_vlan_dict - очікує як аргумент словник із відповідністю інтерфейс-VLAN
  (приклад access_dict)
* access_template - чекає як аргумент списку рядків, які треба додати для
  кожного інтерфейсу (приклад cmd_list)

Функція повинна повертати список усіх портів у режимі access із конфігурацією
на основі шаблону access_cmd_list. Наприкінці рядків у списку не має бути
символу нового рядка. Якщо шаблон access_template має команду switchport
access vlan, додати до неї номер VLANа вказаний у словнику intf_vlan_dict

Перевірити роботу функції на прикладі словника access_dict та списку команд
access_cmd_list. Якщо попередня перевірка пройшла успішно, перевірити роботу
функції ще раз на словнику access_dict_2 та списку команд cmd_list та
переконатися, що у підсумковому списку правильні номери інтерфейсів та вланів.

Приклад роботи функції

In [4]: generate_access_config(access_dict, cmd_list)
Out[4]:
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11']

In [6]: generate_access_config(access_dict_2, access_cmd_list)
Out[6]:
['interface FastEthernet0/3',
 'switchport mode access',
 'switchport access vlan 100',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/7',
 'switchport mode access',
 'switchport access vlan 101',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/9',
 'switchport mode access',
 'switchport access vlan 107',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/10',
 'switchport mode access',
 'switchport access vlan 111',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable']


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""
access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
access_dict_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
    "FastEthernet0/10": 111,
}

access_cmd_list = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
cmd_list = ["switchport mode access", "switchport access vlan"]
