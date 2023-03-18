# -*- coding: utf-8 -*-
"""
Завдання 25.1

Для завдань 25 розділу немає тестів!

Необхідно створити два скрипти:

1. create_db.py
2. add_data.py

1 скрипт create_db.py - в цей скрипт має бути винесена функціональність створення БД:
* повинна виконуватися перевірка наявності файлу БД
* якщо файлу немає, згідно з описом схеми БД у файлі dhcp_snooping_schema.sql,
  має бути створена БД
* ім'я файлу бд - dhcp_snooping.db

У БД має бути дві таблиці (схема описана у файлі dhcp_snooping_schema.sql):
  * switches - в ній знаходяться дані про комутатори
  * dhcp - тут зберігається інформація отримана з виводу sh ip dhcp snooping binding


Приклад виконання скрипту, коли файлу dhcp_snooping.db немає:
$ python create_db.py
Database creation...

Після створення файлу:
$ python create_db.py
Database exists

2 скрипт add_data.py - за допомогою цього скрипта, виконується додавання даних
до БД.  Скрипт повинен додавати дані з виводу sh ip dhcp snooping binding та
інформацію про комутатори.

Відповідно, у файлі add_data.py повинні бути дві частини:
* інформація про комутатори додається до таблиці switches
  * дані про комутатори, знаходяться у файлі switches.yml
* інформація з виводу sh ip dhcp snooping binding додається до таблиці dhcp
  * вивід з трьох комутаторів:
    * файли sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
  * так як таблиця dhcp змінилася, і в ній тепер є поле switch, його потрібно
    також заповнювати. Ім'я комутатора визначається з імені файлу з даними


Приклад виконання скрипту, коли база даних ще не створена:
$ python add_data.py
The database does not exist. Before adding data, you need to create it

Приклад виконання скрипту вперше, після створення бази даних:
$ python add_data.py
Adding data to the switches table...
Add data to dhcp table...


Приклад виконання скрипту, після того, як дані були додані в таблицю (Порядок
додавання даних може бути довільним, але повідомлення повинні виводитися
аналогічно прикладу нижче):

$ python add_data.py
Adding data to the switches table...
While adding data: ('sw1', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
While adding data: ('sw2', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
While adding data: ('sw3', 'London, 21 New Globe Walk') An error occurred: UNIQUE constraint failed: switches.hostname
Adding data to the dhcp table...
While adding data: ('00:09:BB:3D:D6:58', '10.1.10.2', '10', 'FastEthernet0/1', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:04:A3:3E:5B:69', '10.1.5.2', '5', 'FastEthernet0/10', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:05:B3:7E:9B:60', '10.1.5.4', '5', 'FastEthernet0/9', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:07:BC:3F:A6:50', '10.1.10.6', '10', 'FastEthernet0/3', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:09:BC:3F:A6:50', '192.168.100.100', '1', 'FastEthernet0/7', 'sw1') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:E9:BC:3F:A6:50', '100.1.1.6', '3', 'FastEthernet0/20', 'sw3') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:E9:22:11:A6:50', '100.1.1.7', '3', 'FastEthernet0/21', 'sw3') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:A9:BB:3D:D6:58', '10.1.10.20', '10', 'FastEthernet0/7', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:B4:A3:3E:5B:69', '10.1.5.20', '5', 'FastEthernet0/5', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:C5:B3:7E:9B:60', '10.1.5.40', '5', 'FastEthernet0/9', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac
While adding data: ('00:A9:BC:3F:A6:50', '10.1.10.60', '20', 'FastEthernet0/2', 'sw2') An error occurred: UNIQUE constraint failed: dhcp.mac


На даному етапі обидва скрипти викликаються без аргументів.

Код у скриптах має бути розбитий на функції.  Які саме функції та як розділити
код, треба вирішити самостійно.  Частина коду може бути глобальною.
"""
