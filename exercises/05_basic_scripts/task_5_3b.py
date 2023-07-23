# -*- coding: utf-8 -*-
"""
Завдання 5.3b

Переробити скрипт із завдання 5.3a таким чином, щоб при запиті параметра
відображалися доступні параметри. Параметри треба отримати зі словника, не
прописувати вручну.

Вивести інформацію про відповідний параметр, зазначеного пристрою.

Приклад виконання скрипту:
$ python task_5_3b.py
Enter device name: r1
Enter parameter name (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_3b.py
Enter device name: sw1
Enter parameter name (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умов if.
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
parameter = input(f"Enter parameter name ({', '.join(list(london_co[device].keys()))}): ")
print(london_co[device][parameter])
