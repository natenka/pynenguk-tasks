# -*- coding: utf-8 -*-
"""
Завдання 5.3a

Переробити скрипт із завдання 5.3 таким чином, щоб, крім імені пристрою,
запитувався також параметр пристрою, який потрібно відобразити.

Вивести інформацію про відповідний параметр, зазначеного пристрою.

Приклад виконання скрипту:
$ python task_5_3a.py
Enter device name: r1
Enter parameter name: ios
15.4

Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умови if.
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

device = input("Enter device name: ")
parameter = input("Enter parameter name: ")
print(london_co[device][parameter])
