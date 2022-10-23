# -*- coding: utf-8 -*-
"""
Завдання 5.5

Скрипт повинен запитувати у користувача (у такому порядку):
* режим інтерфейсу (access або trunk)
* інтерфейс (тип та номер, виду Gi0/3)
* номер VLAN (для режиму trunk буде вводитися список VLAN)

Залежно від вибраного режиму, на стандартний потік виведення повинна
повертатися відповідна конфігурація access або trunk (шаблони команд
знаходяться в змінних access_template і trunk_template).

При цьому спочатку повинен йти рядок interface і підставлений номер інтерфейсу,
а потім відповідний шаблон, в який підставлений номер VLAN (або список VLAN).

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.

Підказка: у деяких випадках словники можна використовувати як заміну
if/elif/else.

Нижче наведено приклади виконання скрипту, щоб було простіше зрозуміти
завдання.

Приклад виконання скрипта при виборі режиму access:

$ python task_5_5.py
Enter interface mode (access/trunk): access
Enter interface type and number: Fa0/6
Enter VLAN(s) number: 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Приклад виконання скрипта при виборі режиму trunk
$ python task_5_5.py
Enter interface mode (access/trunk): trunk
Enter interface type and number: Fa0/7
Enter VLAN(s) number: 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5

"""

access_template = """switchport mode access
switchport access vlan {}
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable
"""

trunk_template = """switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan {}
"""
