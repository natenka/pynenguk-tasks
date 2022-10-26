# -*- coding: utf-8 -*-
"""
Завдання 17.3

Створити функцію parse_sh_cdp_neighbors, яка обробляє вивід команди show
cdp neighbors.

Функція чекає, як аргумент, на вивід команди одним рядком (не ім'я файлу).
Функція повинна повертати словник, який описує з'єднання між пристроями.

Наприклад, якщо як аргумент було передано такий вивід:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функція повинна повернути такий словник:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Інтерфейси повинні бути записані з пробілом. Тобто так Fa 0/0, а не так Fa0/0.

Перевірити роботу функції на вміст файлу sh_cdp_n_sw1.txt

Приклад виклику функції
In [8]: with open("sh_cdp_n_sw1.txt") as f:
   ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
   ...:
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}}}

In [9]: with open("sh_cdp_n_r1.txt") as f:
   ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
   ...:
{'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}}}

In [10]: with open("sh_cdp_n_r2.txt") as f:
    ...:     pprint(parse_sh_cdp_neighbors(f.read()), sort_dicts=False)
    ...:
{'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
        'Eth 0/1': {'R5': 'Eth 0/0'},
        'Eth 0/2': {'R6': 'Eth 0/1'}}}
"""
