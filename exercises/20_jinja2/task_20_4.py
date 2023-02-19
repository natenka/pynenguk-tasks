# -*- coding: utf-8 -*-
"""
Завдання 20.4

Створіть шаблон templates/add_vlan_to_switch.txt, який буде використовуватись
за необхідності додати VLAN на комутатор.

У шаблоні повинні підтримуватись можливості:
* додавання VLAN та імені VLAN
* додавання VLAN як access, на вказаному інтерфейсі
* додавання VLAN до списку дозволених, на вказані транки

Шаблон треба створювати вручну. Це завдання на синтаксис шаблонів Jinja2.

Якщо VLAN необхідно додати як access, треба налаштувати і режим інтерфейсу і
додати його до VLAN:
interface Gi0/1
 switchport mode access
 switchport access vlan 5

Для транків, необхідно тільки додати VLAN до списку дозволених:
interface Gi0/10
 switchport trunk allowed vlan add 5

Імена змінних треба вибрати на основі прикладу даних у файлі
data_files/add_vlan_to_switch.yaml.

Перевірте шаблон templates/add_vlan_to_switch.txt на даних у файлі
data_files/add_vlan_to_switch.yaml за допомогою функції generate_config із
завдання 20.1. Не копіюйте код функції generate_config.

"""
