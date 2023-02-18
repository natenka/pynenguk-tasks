# -*- coding: utf-8 -*-
"""
Завдання 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.

Приклад роботи функції (ключи в словарях отсортированы из-за pprint)
In [2]: with open("output/sh_ip_int_br.txt") as f:
   ...:     result = parse_output_to_dict("templates/sh_ip_int_br.template", f.read())
   ...:     pprint(result, width=100)
   ...:
[{'address': '15.0.15.1', 'intf': 'FastEthernet0/0', 'protocol': 'up', 'status': 'up'},
 {'address': '10.0.12.1', 'intf': 'FastEthernet0/1', 'protocol': 'up', 'status': 'up'},
 {'address': '10.0.13.1', 'intf': 'FastEthernet0/2', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'FastEthernet0/3', 'protocol': 'up', 'status': 'up'},
 {'address': '10.1.1.1', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
 {'address': '100.0.0.1', 'intf': 'Loopback100', 'protocol': 'up', 'status': 'up'}]

"""
# -*- coding: utf-8 -*-
"""
Завдання 21.1

Создать функцию parse_command_output. Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды sh ip int br с оборудования
и шаблоне templates/sh_ip_int_br.template.

Пример вызова функции
In [5]: with open("output/sh_ip_int_br.txt") as f:
   ...:     pprint(parse_command_output("templates/sh_ip_int_br.template", f.read()))
   ...:
[['intf', 'address', 'status', 'protocol'],
 ['FastEthernet0/0', '15.0.15.1', 'up', 'up'],
 ['FastEthernet0/1', '10.0.12.1', 'up', 'up'],
 ['FastEthernet0/2', '10.0.13.1', 'up', 'up'],
 ['FastEthernet0/3', 'unassigned', 'up', 'up'],
 ['Loopback0', '10.1.1.1', 'up', 'up'],
 ['Loopback100', '100.0.0.1', 'up', 'up']]

"""
from netmiko import ConnectHandler


# вызов функции должен выглядеть так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.139.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)
# -*- coding: utf-8 -*-
"""
Завдання 21.2

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding
и записать его в файл templates/sh_ip_dhcp_snooping.template

Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* mac - такого вида 00:04:A3:3E:5B:69
* ip - такого вида 10.1.10.6
* vlan - 10
* intf - FastEthernet0/10

Проверить работу шаблона с помощью функции parse_command_output из задания 21.1.
"""
# -*- coding: utf-8 -*-
"""
Завдання 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и sh version.

Пример вызова функции для sh ip int br

In [8]: attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}
   ...: with open("output/sh_ip_int_br.txt") as f:
   ...:     pprint(parse_command_dynamic(f.read(), attributes), width=120)
   ...:
[{'address': '15.0.15.1', 'intf': 'FastEthernet0/0', 'protocol': 'up', 'status': 'up'},
 {'address': '10.0.12.1', 'intf': 'FastEthernet0/1', 'protocol': 'up', 'status': 'up'},
 {'address': '10.0.13.1', 'intf': 'FastEthernet0/2', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'FastEthernet0/3', 'protocol': 'up', 'status': 'up'},
 {'address': '10.1.1.1', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
 {'address': '100.0.0.1', 'intf': 'Loopback100', 'protocol': 'up', 'status': 'up'}]

Пример вызова функции для sh version

In [9]: attributes = {'Command': 'sh version', 'Vendor': 'cisco_ios'}
   ...: with open("output/sh_version.txt") as f:
   ...:     output = f.read()
   ...: print(parse_command_dynamic(output, attributes))

[{'version': '15.3(2)S1', 'hostname': 'R1_LONDON'}]

"""
# -*- coding: utf-8 -*-
"""
Завдання 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.

Пример вызова функции
In [17]: result = send_and_parse_show_command(
    ...:     devices[1], "sh ip int br", templates_path=full_pth
    ...: )
    ...: pprint(result, width=120)
    ...:
[{'address': '192.168.100.2', 'intf': 'Ethernet0/0', 'protocol': 'up', 'status': 'up'},
 {'address': '10.100.23.2', 'intf': 'Ethernet0/1', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Ethernet0/2', 'protocol': 'down', 'status': 'administratively down'},
 {'address': 'unassigned', 'intf': 'Ethernet0/3', 'protocol': 'down', 'status': 'administratively down'},
 {'address': '10.2.2.2', 'intf': 'Loopback0', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Loopback9', 'protocol': 'up', 'status': 'up'},
 {'address': 'unassigned', 'intf': 'Loopback19', 'protocol': 'up', 'status': 'up'},
 {'address': '10.100.100.2', 'intf': 'Loopback100', 'protocol': 'up', 'status': 'up'},
 {'address': '10.255.1.2', 'intf': 'Tunnel2', 'protocol': 'down', 'status': 'up'}]

"""
# -*- coding: utf-8 -*-
"""
Завдання 21.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в
параллельных потоках функцию send_and_parse_show_command из задания 21.4.

Параметры функции send_and_parse_command_parallel:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* templates_path - путь к каталогу с шаблонами TextFSM
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать словарь:
* ключи - IP-адрес устройства с которого получен вывод
* значения - список словарей (вывод который возвращает функция send_and_parse_show_command)

Пример словаря:
{'192.168.100.1': [{'address': '192.168.100.1',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '192.168.200.1',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}],
 '192.168.100.2': [{'address': '192.168.100.2',
                    'intf': 'Ethernet0/0',
                    'protocol': 'up',
                    'status': 'up'},
                   {'address': '10.100.23.2',
                    'intf': 'Ethernet0/1',
                    'protocol': 'up',
                    'status': 'up'}]}

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
