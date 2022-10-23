# -*- coding: utf-8 -*-
"""
Завдання 4.2

Якщо запустити код завдання, буде такий вивід:
$ python task_4_2.py
ip nat inside source list ACL interface FastEthernet0/1 overload

Треба змінити рядок nat таким чином, щоб на екран було виведено такий рядок
(замінено тип інтерфейсу з FastEthernet на GigabitEthernet і рядок переведено в
нижній регістр):

$ python task_4_2.py
ip nat inside source list acl interface gigabitethernet0/1 overload

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.

"""

nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
