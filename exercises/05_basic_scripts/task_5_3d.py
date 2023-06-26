# -*- coding: utf-8 -*-
"""
Завдання 5.3d

Переробити скрипт із завдання 5.3c таким чином, щоб при запиті параметра
користувач міг вводити назву параметра в будь-якому регістрі.

Приклад виконання скрипту:
$ python task_5_3d.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): IOS
15.4


Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умови if.

Важливий момент: для того щоб тест пройшов, текст запиту треба писати саме в
input, а не в print. Тобто так:
device = input("Enter device name: ")

а не так:
print("Enter device name: ")
device = input()
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}
