# -*- coding: utf-8 -*-
"""
Завдання 17.3a

Створити функцію generate_topology_from_cdp, яка обробляє вивід команди show
cdp neighbor з декількох файлів та записує підсумкову топологію до одного
словника.

Функція generate_topology_from_cdp має бути створена з параметрами:
* list_of_files - список файлів з яких треба зчитати вивід команди sh cdp neighbor
* save_to_filename - ім'я файлу у форматі YAML, у якому зберігається топологія.
 * Значення за замовчуванням - None. За замовчанням топологія не зберігається у файлі
 * топологія зберігається тільки, якщо save_to_filename як аргумент вказано ім'я файлу

Функція повинна повертати словник, який описує з'єднання між пристроями,
незалежно від того, чи зберігається топологія у файл.

Структура словника має бути такою:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Інтерфейси повинні бути записані з пробілом. Тобто так Fa 0/0, а не так Fa0/0.

Перевірити роботу функції generate_topology_from_cdp на списку файлів:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Перевірити роботу параметра save_to_filename та записати отриманий словник у
файл topology.yaml. Він знадобиться у наступному завданні.

Приклад виклику функції
In [11]: pprint(generate_topology_from_cdp(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt"]), sort_dicts=False)
{'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}},
 'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}}}

In [12]: f_list
Out[12]:
['sh_cdp_n_r2.txt',
 'sh_cdp_n_r5.txt',
 'sh_cdp_n_r1.txt',
 'sh_cdp_n_sw1.txt',
 'sh_cdp_n_r3.txt',
 'sh_cdp_n_r4.txt',
 'sh_cdp_n_r6.txt']

In [13]: pprint(generate_topology_from_cdp(f_list), sort_dicts=False)
{'R2': {'Eth 0/0': {'SW1': 'Eth 0/2'},
        'Eth 0/1': {'R5': 'Eth 0/0'},
        'Eth 0/2': {'R6': 'Eth 0/1'}},
 'R5': {'Eth 0/0': {'R2': 'Eth 0/1'}, 'Eth 0/1': {'R4': 'Eth 0/1'}},
 'R1': {'Eth 0/0': {'SW1': 'Eth 0/1'}},
 'SW1': {'Eth 0/1': {'R1': 'Eth 0/0'},
         'Eth 0/2': {'R2': 'Eth 0/0'},
         'Eth 0/3': {'R3': 'Eth 0/0'},
         'Eth 0/4': {'R4': 'Eth 0/0'}},
 'R3': {'Eth 0/0': {'SW1': 'Eth 0/3'}},
 'R4': {'Eth 0/0': {'SW1': 'Eth 0/4'}, 'Eth 0/1': {'R5': 'Eth 0/1'}},
 'R6': {'Eth 0/1': {'R2': 'Eth 0/2'}}}
"""
