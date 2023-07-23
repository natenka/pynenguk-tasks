# -*- coding: utf-8 -*-
"""
Завдання 5.3

У завданні створено словник, з інформацією про різні пристрої.

Необхідно запитати користувача ввести ім'я пристрою (r1, r2 або sw1). І вивести
інформацію про відповідний пристрій стандартний потік виведення (інформація
буде у вигляді словника).

Приклад виконання скрипту:
$ python task_5_3.py
Enter device name: r1
{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

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

user_input = input("Enter device name: ")
print(london_co[user_input])
