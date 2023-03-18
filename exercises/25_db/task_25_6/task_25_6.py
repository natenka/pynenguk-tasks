# -*- coding: utf-8 -*-
"""
Завдання 25.6

Для завдань 25 розділу немає тестів!

У цьому завданні викладено файл parse_dhcp_snooping.py.
У файлі parse_dhcp_snooping.py нічого не можна змінювати.

У файлі створено кілька функцій та описано аргументи командного рядка, які
приймає скрипт.  Є підтримка аргументів для виконання всіх дій, які у
попередніх завданнях виконувались у файлах create_db.py, add_data.py і
get_data.py.

У файлі parse_dhcp_snooping.py є такий рядок:
import parse_dhcp_snooping_functions as pds

І завдання завдання в тому, щоб створити всі необхідні функції, у файлі
parse_dhcp_snooping_functions.py на основі інформації у файлі
parse_dhcp_snooping.py.

З файлу parse_dhcp_snooping.py необхідно визначити:
* які функції мають бути у файлі parse_dhcp_snooping_functions.py
* які параметри створити у цих функціях

Необхідно створити відповідні функції та перенести в них функціонал, описаний у
попередніх завданнях.

Вся необхідна інформація присутня у функціях create, add, get, у файлі
parse_dhcp_snooping.py.

В принципі, для виконання завдання не обов'язково розбиратися з модулем
argparse, але, можна почитати про нього в розділі
https://pyneng.readthedocs.io/uk/latest/book/additional_info/argparse.html

Для того, щоб було простіше розпочати, спробуйте створити необхідні функції у
файлі parse_dhcp_snooping_functions.py та просто виведіть аргументи функцій,
використовуючи print.

Потім можна створити функції, які запитують інформацію з БД (базу даних можна
скопіювати з попередніх завдань).

Можна створювати будь-які допоміжні функції у файлі parse_dhcp_snooping_functions.py,
а не лише ті, що викликаються з файлу parse_dhcp_snooping.py.

Перевірте всі операції:
* створення БД
* додавання інформації про комутатори
* додавання інформації sh ip dhcp snooping binding із файлів
* вибірку інформації з БД (за параметром і всю інформацію)

Щоб було простіше зрозуміти, як виглядатиме виклик скрипта, нижче кілька
прикладів. У прикладах показується варіант, коли базі даних є поля active і
last_active, але можна також використовувати варіант без цих полів.


$ python parse_dhcp_snooping.py get -h
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]

optional arguments:
  -h, --help            show this help message and exit
  --db DB_FILE          database name
  -k {mac,ip,vlan,interface,switch}
                        parameter for searching records
  -v VALUE              parameter value
  -a                    show all database content


$ python parse_dhcp_snooping.py add -h
usage: parse_dhcp_snooping.py add [-h] [--db DB_FILE] [-s]
                                  filename [filename ...]

positional arguments:
  filename      file(s) to add

optional arguments:
  -h, --help    show this help message and exit
  --db DB_FILE  database name
  -s            if the flag is set, add switch data, otherwise add DHCP
                records


$ python parse_dhcp_snooping.py create_db
Creating a dhcp_snooping.db database with dhcp_snooping_schema.sql schema
Creating database...


$ python parse_dhcp_snooping.py add sw[1-3]_dhcp_snooping.txt
Adding information from files
sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt

Adding data on DHCP records to dhcp_snooping.db


$ python parse_dhcp_snooping.py add -s switches.yml
Adding switch data

$ python parse_dhcp_snooping.py get
The dhcp table has the following entries:

Active entries:

-----------------  ---------------  --  ----------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2        10  FastEthernet0/1   sw1  1  2019-03-08 16:47:52
00:04:A3:3E:5B:69  10.1.5.2          5  FastEthernet0/10  sw1  1  2019-03-08 16:47:52
00:05:B3:7E:9B:60  10.1.5.4          5  FastEthernet0/9   sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6        10  FastEthernet0/3   sw1  1  2019-03-08 16:47:52
00:09:BC:3F:A6:50  192.168.100.100   1  FastEthernet0/7   sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20       10  FastEthernet0/7   sw2  1  2019-03-08 16:47:52
00:B4:A3:3E:5B:69  10.1.5.20         5  FastEthernet0/5   sw2  1  2019-03-08 16:47:52
00:C5:B3:7E:9B:60  10.1.5.40         5  FastEthernet0/9   sw2  1  2019-03-08 16:47:52
00:A9:BC:3F:A6:50  10.1.10.60       20  FastEthernet0/2   sw2  1  2019-03-08 16:47:52
00:E9:BC:3F:A6:50  100.1.1.6         3  FastEthernet0/20  sw3  1  2019-03-08 16:47:52
-----------------  ---------------  --  ----------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vlan -v 10
Data from the database: dhcp_snooping.db
Information about devices with the following parameters: vlan 10

Active entries:

-----------------  ----------  --  ---------------  ---  -  -------------------
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1  2019-03-08 16:47:52
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/3  sw1  1  2019-03-08 16:47:52
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1  2019-03-08 16:47:52
-----------------  ----------  --  ---------------  ---  -  -------------------


$ python parse_dhcp_snooping.py get -k vln -v 10
usage: parse_dhcp_snooping.py get [-h] [--db DB_FILE]
                                  [-k {mac,ip,vlan,interface,switch}]
                                  [-v VALUE] [-a]
parse_dhcp_snooping.py get: error: argument -k: invalid choice: 'vln' (choose from 'mac', 'ip', 'vlan', 'interface', 'switch')
"""
