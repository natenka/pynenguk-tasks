# -*- coding: utf-8 -*-
"""
Завдання 9.5

Створити функцію generate_trunk_config, яка створює конфігурацію для trunk-портів.

Функція повинна мати такі параметри:
* intf_vlan_dict: очікує як аргумент словник з відповідністю інтерфейс-VLANи
  (приклад trunk_dict)
* trunk_template: Очікує як аргумент шаблон конфігурації trunk-портів у вигляді
  списку команд (приклад trunk_cmd_list)

Функція повинна повертати список команд із конфігурацією на основі вказаних
портів та шаблону trunk_cmd_list. Наприкінці рядків у списку не має бути символ
нового рядка. Якщо у шаблоні trunk_template є команда switchport trunk
allowed vlan, додати до неї владу вказану у словнику intf_vlan_dict.

Перевірити роботу функції на прикладі словника trunk_dict та списку команд
trunk_cmd_list. Якщо попередня перевірка пройшла успішно, перевірити роботу
функції ще раз на словнику trunk_dict_2 та переконається, що у підсумковому
списку правильні номери інтерфейсів та вланів.


Приклад роботи функції
In [8]: generate_trunk_config(trunk_dict, trunk_cmd_list)
Out[8]:
['interface FastEthernet0/1',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 10,20,30',
 'interface FastEthernet0/2',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 11,30',
 'interface FastEthernet0/4',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 17']

In [9]: generate_trunk_config(trunk_dict_2, trunk_cmd_list)
Out[9]:
['interface FastEthernet0/11',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 120,131',
 'interface FastEthernet0/15',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 111,130',
 'interface FastEthernet0/14',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 117']


У завданнях 9го розділу і далі, крім зазначеної функції, можна створювати
будь-які додаткові функції.
"""

trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_dict_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
