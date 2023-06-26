# -*- coding: utf-8 -*-
"""
Завдання 5.3c

Переробити скрипт із завдання 5.3b таким чином, щоб при запиті параметра, якого
немає у словнику пристрою, відображалося повідомлення 'There is no such parameter'.
Завдання стосується лише параметрів пристроїв, не самих пристроїв.

Спробуйте набрати неправильне ім'я параметра або неіснуючий параметр, щоб
побачити результат. А потім виконуйте завдання.

Якщо вибрано існуючий параметр, вивести інформацію про відповідний параметр,
вказаний у пристрої.

Приклад виконання скрипту:
$ python task_5_3c.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): ips
There is no such parameter

Обмеження: не можна змінювати словник london_co.

Це завдання можна зробити без використання умов if.

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
