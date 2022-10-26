# -*- coding: utf-8 -*-
"""
Завдання 18.1

Створити функцію send_show_command.
Функція підключається SSH (за допомогою netmiko) до ОДНОГО пристрою і виконує
вказану команду.

Параметри функції:
* device - словник із параметрами підключення до пристрою
* command – команда, яку треба виконати

Функція повертає рядок із виводом команди.

Скрипт повинен надсилати команду command на всі пристрої з файлу devices.yaml
за допомогою функції send_show_command (ця частина коду написана).

У цьому розділі тести перевіряють підключення на пристроях у файлі
devices.yaml. Якщо параметри підключення до ваших пристроїв відрізняються,
потрібно змінити параметри у файлі devices.yaml.
"""
import yaml


if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))
