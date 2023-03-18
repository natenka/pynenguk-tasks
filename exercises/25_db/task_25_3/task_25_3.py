# -*- coding: utf-8 -*-
"""
Завдання 25.3

Для завдань 25 розділу немає тестів!

У попередніх завданнях інформація додавалася до порожньої БД.  У цьому завдання
розбирається ситуація, коли в БД вже є інформація.

Скопіюйте скрипт add_data.py із завдання 25.1 і спробуйте виконати його
повторно на існуючій базі даних.

Швидше за все, ви отримаєте такий результат:
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
... (the command output is abbreviated)


При створенні схеми БД, було явно зазначено, що поле MAC-адреса має бути
унікальним. Тому при додаванні запису з такою ж MAC-адресою виникає виняток
(помилка). У завданні 25.1 виняток обробляється та виводиться повідомлення на
стандартний потік виведення.

У цьому завданні вважається, що інформація періодично зчитується з комутаторів
та записується у файли. Після цього інформацію з файлів треба перенести до бази
даних.

При цьому в нових даних можуть бути зміни: MAC зник, MAC перейшов на інший
порт/vlan, з'явився новий MAC тощо.  У цьому завданні в таблиці dhcp треба
створити нове поле active, яке вказуватиме чи є запис актуальним.  Нова схема
БД знаходиться у файлі dhcp_snooping_schema.sql

Поле active має приймати такі значення:
* 0 – означає False. Використовується для того, щоб відзначити запис як неактивний
* 1 - True. Використовується, щоб вказати, що запис активний

Щоразу, коли інформація з файлів із виведенням DHCP snooping додається знову,
треба позначити всі існуючі записи (для цього комутатора) як неактивні (active = 0).
Потім ви можете оновити інформацію та позначити нові записи як активні (active = 1).

Таким чином, у БД залишаться і старі записи для MAC-адрес, які зараз не
активні, і з'явиться оновлена інформація для активних адрес.

Наприклад, у таблиці dhcp такі записи:
mac                ip          vlan        interface         switch      active
-----------------  ----------  ----------  ----------------  ----------  ----------
00:09:BB:3D:D6:58  10.1.10.2   10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.5.2    5           FastEthernet0/10  sw1         1
00:05:B3:7E:9B:60  10.1.5.4    5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6   10          FastEthernet0/3   sw1         1
00:09:BC:3F:A6:50  192.168.10  1           FastEthernet0/7   sw1         1


І треба додати таку інформацію з файлу:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:09:BB:3D:D6:58   10.1.10.2        86250       dhcp-snooping   10    FastEthernet0/1
00:04:A3:3E:5B:69   10.1.15.2        63951       dhcp-snooping   15    FastEthernet0/15
00:05:B3:7E:9B:60   10.1.5.4         63253       dhcp-snooping   5     FastEthernet0/9
00:07:BC:3F:A6:50   10.1.10.6        76260       dhcp-snooping   10    FastEthernet0/5


Після додавання даних таблиця має виглядати так:
mac                ip               vlan        interface         switch      active
-----------------  ---------------  ----------  ---------------   ----------  ----------
00:09:BC:3F:A6:50  192.168.100.100  1           FastEthernet0/7   sw1         0
00:09:BB:3D:D6:58  10.1.10.2        10          FastEthernet0/1   sw1         1
00:04:A3:3E:5B:69  10.1.15.2        15          FastEthernet0/15  sw1         1
00:05:B3:7E:9B:60  10.1.5.4         5           FastEthernet0/9   sw1         1
00:07:BC:3F:A6:50  10.1.10.6        10          FastEthernet0/5   sw1         1

Нова інформація має перезаписувати попередню:
* MAC 00:04:A3:3E:5B:69 перейшов на інший порт, потрапив в інший інтерфейс і
  отримав іншу IP адресу
* MAC 00:07:BC:3F:A6:50 перейшов на інший порт


Якщо якогось MAC-адреси немає у новому файлі, його треба залишити в бд зі
значенням active = 0:
* MAC-адреси 00:09:BC:3F:A6:50 немає в новій інформації (вимкнули комп)

Змініть скрипт add_data.py таким чином, щоб виконувалися нові умови та
заповнювалось поле active.

Код у скрипті має бути розбитий на функції.  Які саме функції та як розділити
код, треба вирішити самостійно.  Частина коду може бути глобальною.

> Для перевірки коректності запиту SQL, можна виконати його в командному рядку
> за допомогою утиліти sqlite3.

Для перевірки завдання та роботи нового поля спочатку додайте в бд інформацію з
файлів sw*_dhcp_snooping.txt, а потім додайте інформацію з файлів
new_data/sw*_dhcp_snooping.txt.

Дані мають виглядати так (порядок рядків може бути будь-яким)
-----------------  ---------------  --  ----------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  0
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  0
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2        15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7         3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65       20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77       10  FastEthernet0/4   sw2  1
-----------------  ---------------  --  ----------------  ---  -


"""
