# -*- coding: utf-8 -*-
"""
Завдання 4.7

Перетворити MAC-адресу в рядку mac на двійковий рядок такого виду:
'101010101010101010111011101110111100110011001100'

Отриманий новий рядок вивести стандартний потік виведення (stdout) за допомогою
print.

Підказка: MAC-адреса без: це шістнадцяткове число AAAABBBBCCCC.

Попередження: у розділі 4 тести можна легко "обдурити", зробивши потрібний
вивід print, без отримання результатів з даних завдання за допомогою Python. Це
не означає, що завдання зроблено правильно, просто на даному етапі складно
інакше перевіряти результат.
"""

mac = "AAAA:BBBB:CCCC"
new_mac = int(mac.replace(":", ""), 16)
print(f"{new_mac:0>8b}")
