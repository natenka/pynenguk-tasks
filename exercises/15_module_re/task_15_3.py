# -*- coding: utf-8 -*-
"""
Завдання 15.3

Створити функцію convert_ios_nat_to_asa, яка конвертує правила NAT із
синтаксису cisco IOS в cisco ASA.

Функція чекає на такі аргументи:
* ім'я файлу, в якому міститься правила NAT Cisco IOS
* ім'я файлу, в який потрібно записати отримані правила NAT для ASA

Функція нічого не повертає.
Перевірити функцію на файлі cisco_nat_config.txt.

Приклад правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

І відповідні правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

У файлі з правилами для ASA:
* не повинно бути порожніх рядків між правилами
* перед рядками "object network" не повинні бути прогалини
* перед рештою рядків має бути одна пропуск

У всіх правилах для ASA інтерфейси будуть однаковими (inside, outside).

"""
