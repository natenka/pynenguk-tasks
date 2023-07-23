# -*- coding: utf-8 -*-
"""
Завдання 5.5a

Доповнити скрипт із завдання 5.5 таким чином, щоб, залежно від вибраного
режиму, задавалися різні запитання у запиті про номер VLAN або список VLANів:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter the allowed VLANs:'

Плюсом буде вирішити завдання без використання умови if та циклу for, але
перший варіант рішення краще зробити так, як виходитиме.
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

user_int_mode = input("Enter interface mode (access/trunk): ")
user_int_type = input("Enter interface type and number: ")

template_int = """
interface {}
"""

if user_int_mode == "access":
    user_vlans_number = input("Enter VLAN number: ")
    print(template_int.format(user_int_type))
    print(access_template.format(user_vlans_number))
elif user_int_mode == "trunk":
    user_vlans_number = input("Enter the allowed VLANs: ")
    print(template_int.format(user_int_type))
    print(trunk_template.format(user_vlans_number))
