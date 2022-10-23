# -*- coding: utf-8 -*-
"""
Завдання 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.2a

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
выводить на экран строки из конфига, исключая некоторые.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_2a.py config_sw1.txt

Вывести на стандартный поток вывода команды из переданного конфигурационного
файла, исключая строки, которые начинаются с '!' и строки в которых содержатся
слова из списка ignore.
Вывод не должен содержать пустые строки.

Пример вывода:
$ python task_7_2a.py config_sw1.txt
version 15.0
hostname sw1
interface Ethernet0/0
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet0/2
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 spanning-tree portfast edge trunk
interface Ethernet1/0
interface Ethernet1/1
interface Ethernet1/2
interface Ethernet1/3
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport input all

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
Завдання 7.2b

Скопировать код из задания 7.2a и переделать его: вместо вывода на стандартный
поток вывода, скрипт должен записать полученные строки в файл.

Имена файлов нужно передавать как аргументы скрипту:
1 аргумент имя исходного файла конфигурации
2 аргумент имя итогового файла конфигурации, в который будут записаны строки

Пример вызова:
$ python task_7_2b.py config_sw1.txt new_config.txt

При этом, должны быть отфильтрованы строки со словами, которые содержатся в списке ignore
и строки, которые начинаются на '!'.
"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
Завдання 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
выводить на экран строки из конфига, исключая некоторые.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_2.py config_sw1.txt

Вывести на стандартный поток вывода команды из переданного конфигурационного
файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Пример вывода:
$ python task_7_2.py config_sw1.txt
Current configuration : 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
 duplex auto
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
interface Ethernet0/2
 duplex auto
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
...

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3a

Сделать копию скрипта задания 7.3.

Переделать скрипт: Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Подсказка: Для сортировки удобно сначала создать список списков такого типа,
а потом сортировать.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

Сортировка должна быть по первому элементу (vlan), а если первый элемент одинаковый,
то по второму. Так работает по умолчанию функция sorted и метод sort, если сортировать
список списков выше.

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Приклад роботи скрипта:
$ python task_7_3b.py
Введите номер влана: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt. Каждая строка,
где есть MAC-адрес, должна быть обработана таким образом, чтобы
на стандартный поток вывода была выведена таблица вида:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9

"""
# -*- coding: utf-8 -*-
"""
Завдання 7.4

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о портах в режиме trunk и вланах, которые настроены
на этих портах.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь портов в режиме trunk, где ключи номера портов,
а значения список разрешенных VLAN (список строк).

Записать итоговый словарь в переменную trunk_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}


Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

Подсказка по синтаксису cisco: в этом задании считаем, что интерфейс находится
в режиме trunk, если у него настроена команда switchport trunk allowed vlan.
"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
Завдання 7.5

Создать скрипт, который будет обрабатывать конфигурационный файл коммутатора и
получать из него информацию о конфигурации интерфейсов.

Имя файла конфигурации передается как аргумент скрипту.
$ python task_7_5.py config_trunk_sw2.txt
$ python task_7_5.py config_trunk_sw3.txt

Передавать имя файла как аргумент скрипту. Указанный конфиг надо обработать и
получить словарь где ключи имя интерфейса, а значение список команд, которые
начинаются на switchport. Команды в списке должны быть без пробела в начале
строки и перевода строки в конце.

Записать итоговый словарь в переменную interface_dict (именно эта переменная будет
проверяться в тесте). По желанию можно выводить словарь на экран, тест
проверяет только содержимое переменной. Тут удобно выводить словарь с помощью pprint.

Например, для файла config_trunk_sw2.txt должен получиться такой словарь:

$ python task_7_5.py config_trunk_sw2.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,200',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 100,300,400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/4': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 400,500,600',
                     'switchport mode trunk'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport mode access',
                     'switchport access vlan 20']}

Для файла config_trunk_sw3.txt должен получиться такой словарь:
$ python task_7_5.py config_trunk_sw3.txt
{'FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,20,21,22',
                     'switchport mode trunk'],
 'FastEthernet0/2': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 10,13,1450,1451,1452',
                     'switchport mode trunk'],
 'FastEthernet0/3': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/4': ['switchport mode access',
                     'switchport access vlan 20'],
 'FastEthernet0/5': ['switchport mode access',
                     'switchport access vlan 30'],
 'FastEthernet0/6': ['switchport trunk encapsulation dot1q',
                     'switchport trunk allowed vlan 40,50,60',
                     'switchport mode trunk'],
 'FastEthernet0/7': ['switchport mode access'],
 'FastEthernet0/8': ['switchport mode access']}

Проверить работу функции на примере файлов config_trunk_sw2.txt и config_trunk_sw3.txt.
Убедиться, что для этих файлов получаются правильные словари.

"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
Завдання 9.0

Пройти всі питання в pquiz по розділу 09.
Перед проходженням питань оновити pyneng-quiz:
$ pip install -U pyneng-quiz

Запуск:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
Завдання 9.1

Создать функцию convert_mac, которая конвертирует MAC-адрес из формата
1a1b.2c2d.3e3f в 1a:1b:2c:2d:3e:3f.

У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в формате 1a1b.2c2d.3e3f.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Проверить работу функции на разных MAC-адресах в списке mac_list.

В этом задании можно не проверять, что MAC-адрес, который передается функции
как аргумент записан в формате "aaaa.bbbb.cccc". Это будет сделано в задании 11го
раздела.

Пример работы функции:

In [4]: convert_mac("1a1b.2c2d.3e3f")
Out[4]: '1a:1b:2c:2d:3e:3f'

In [5]: convert_mac("1111.2222.3333")
Out[5]: '11:11:22:22:33:33'

In [6]: mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

In [7]: for m in mac_list:
   ...:     print(convert_mac(m))
   ...:
1a:1b:2c:2d:3e:3f
aa:aa:bb:bb:cc:cc
11:11:22:22:33:33

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

# -*- coding: utf-8 -*-
"""
Завдання 9.2

Создать функцию check_ip, которая проверяет, что строка, которая была передана функции,
содержит правильный IP-адрес.

Адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255

У функции должен быть один параметр ip_addr, который ожидает строку с IP-адресом.
Функция должна возвращать True если адрес правильный, False иначе.

Проверить работу функции на строках в списке ip_list.
Пример работы функции:
In [3]: check_ip("10.1.1.1")
Out[3]: True

In [4]: check_ip("10.500.1.1")
Out[4]: False

In [5]: check_ip("10.a.b.1")
Out[5]: False

In [6]: check_ip("10.1.1.1.")
Out[6]: False

In [7]: check_ip("10.1.1.1.1")
Out[7]: False

In [8]: check_ip("10.1.1.")
Out[8]: False

In [9]: check_ip("10.1.1")
Out[9]: False

In [10]: for ip in ip_list:
    ...:     print(check_ip(ip))
    ...:
True
False
False
True
False

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ip_list = ["10.1.1.1", "10.3.a.a", "500.1.1.1", "150.168.100.1", "62.150.240.300"]
# -*- coding: utf-8 -*-
"""
Завдання 9.3a

Создать функцию clean_config.  Функция clean_config обрабатывает
конфигурационный файл и возвращает список команд из указанного
конфигурационного файла.

У функции clean_config должны быть такие параметры:
* config_filename - ожидает как аргумент имя конфигурационного файла
* ignore_lines - ожидает как аргумент список строк, которые надо игнорировать.
  Значение по умолчанию None. То есть по умолчанию никакие строки не игноруются
* ignore_exclamation - контролирует то игнорируются ли строки, которые
  начинаются с восклицательного знака. Возможные значения True/False.
  Значение по умолчанию True
* strip_lines - контролирует удаление пробела в начале строки и перевода строки в конце.
  True - удалить пробелы в начале строки и перевод в конце, False - не удалять.
  Возможные значения True/False. Значение по умолчанию False
* delete_empty_lines - контролирует удаление пустых строк. True - удалять, False - нет.
  Возможные значения True/False. Значение по умолчанию True

Для удобства все значения по умолчанию для необязательных параметров:
* ignore_lines - None
* ignore_exclamation - True
* delete_empty_lines - True
* strip_lines - False

Функция clean_config обрабатывает конфигурационный файл и возвращает список
команд из указанного конфигурационного файла:
* если в параметр ignore_lines передан список строк - исключая строки конфигурации,
  в которых содержатся строки из списка ignore_lines.
* если ignore_exclamation равно True - исключая строки которые начинаются с '!'
* если delete_empty_lines равно True - исключая пустые строки
* если strip_lines равно True - строки в списке должны быть без пробелов в начале
  и перевода строки в конце строки


Пример работы функции:
In [3]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list, ignore_exclamation=False)
Out[3]:
['hostname PE_r3',
 '!',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '!',
 '!',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '!',
 '!',
 '!',
 'alias configure sh do sh',
 '!',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [4]: clean_config("config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list)
Out[4]:
['hostname PE_r3',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'alias configure sh do sh',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']

In [5]: clean_config("config_r3_short.txt", strip_lines=True, delete_empty_lines=False)
Out[5]:
['hostname PE_r3',
 '',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 '',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 '',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec bri show ip int bri | exc unass',
 'line con 0',
 'exec-timeout 0 0',
 'privilege level 15',
 'logging synchronous']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
Завдання 9.3

Создать функцию clean_config.

У функции clean_config должно быть два параметра:
* config_filename - ожидает как аргумент имя конфигурационного файла
* ignore_lines - ожидает как аргумент список строк, которые надо игнорировать

Функция clean_config обрабатывает конфигурационный файл и возвращает список
команд из указанного конфигурационного файла, исключая строки конфигурации,
которые начинаются с '!' и строки конфигурации в которых содержатся строки из
списка ignore_lines.
Команды в списке должны быть без перевода строки в конце строки.

Проверить работу функции на примере файла config_sw1.txt, config_sw2.txt,
config_r1.txt и списка ignore_list.

Пример работы функции:
In [2]: clean_config("config_r2_short.txt", ignore_list)
Out[2]:
['version 15.2',
 'hostname PE_r2',
 'no ip http server',
 'no ip http secure-server',
 'ip route 10.2.2.2 255.255.255.255 Tunnel0',
 'ip access-list standard LDP',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'line con 0',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 'line aux 0',
 'line vty 0 4',
 ' login',
 ' transport input all']

In [7]: clean_config("config_r2_short.txt", ["ip", "service", "line"])
Out[7]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 'alias configure sh do sh',
 'alias exec ospf sh run | s ^router ospf',
 'alias exec id show int desc',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']

In [8]: clean_config("config_r2_short.txt", ["ip", "service", "line", "alias"])
Out[8]:
['Current configuration : 4052 bytes',
 'version 15.2',
 'hostname PE_r2',
 ' deny   10.0.0.0 0.0.255.255',
 ' permit 10.0.0.0 0.255.255.255',
 'mpls ldp router-id Loopback0 force',
 'control-plane',
 ' exec-timeout 0 0',
 ' privilege level 15',
 ' logging synchronous',
 ' login',
 ' transport input all']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
Завдання 9.4

Создать функцию generate_access_dict, которая генерирует конфигурацию
для access-портов.

У функции должно быть два параметра:
* intf_vlan_dict - ожидает как аргумент словарь с соответствием интерфейс-VLAN
  (пример access_dict)
* access_template - ожидает как аргумент список строк, которые надо добавить
  для каждого интерфейсы (пример cmd_list)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_cmd_list. В конце строк в списке не должно быть
символа перевода строки.
Если в шаблоне access_template есть команда switchport access vlan, добавить к
ней номер влана указанный в словаре intf_vlan_dict

Проверить работу функции на примере словаря access_dict и списка команд
access_cmd_list.  Если предыдущая проверка прошла успешно, проверить работу
функции еще раз на словаре access_dict_2 и списке команд cmd_list и убедиться,
что в итоговом списке правильные номера интерфейсов и вланов.

Пример работы функции

In [4]: generate_access_dict(access_dict, cmd_list)
Out[4]:
['interface FastEthernet0/12',
 'switchport mode access',
 'switchport access vlan 10',
 'interface FastEthernet0/14',
 'switchport mode access',
 'switchport access vlan 11']

In [6]: generate_access_config(access_dict_2, access_cmd_list)
Out[6]:
['interface FastEthernet0/3',
 'switchport mode access',
 'switchport access vlan 100',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/7',
 'switchport mode access',
 'switchport access vlan 101',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/9',
 'switchport mode access',
 'switchport access vlan 107',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable',
 'interface FastEthernet0/10',
 'switchport mode access',
 'switchport access vlan 111',
 'switchport nonegotiate',
 'spanning-tree portfast',
 'spanning-tree bpduguard enable']


Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
access_dict = {"FastEthernet0/12": 10, "FastEthernet0/14": 11}
access_dict_2 = {
    "FastEthernet0/3": 100,
    "FastEthernet0/7": 101,
    "FastEthernet0/9": 107,
    "FastEthernet0/10": 111,
}

access_cmd_list = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]
cmd_list = ["switchport mode access", "switchport access vlan"]
# -*- coding: utf-8 -*-
"""
Завдання 9.5a

Сделать копию функции generate_trunk_config из задания 9.5

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict и шаблона trunk_cmd_list.

Пример работы функции
In [2]: pprint(generate_trunk_config(trunk_dict, trunk_cmd_list))
{'FastEthernet0/1': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 10,20,30'],
 'FastEthernet0/2': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 11,30'],
 'FastEthernet0/4': ['switchport mode trunk',
                     'switchport trunk native vlan 999',
                     'switchport trunk allowed vlan 17']}

В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""


trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}
# -*- coding: utf-8 -*-
"""
Завдання 9.5

Создать функцию generate_trunk_config, которая генерирует
конфигурацию для trunk-портов.

У функции должны быть такие параметры:

- intf_vlan_dict: ожидает как аргумент словарь с соответствием интерфейс-VLANы
  (пример trunk_dict)
- trunk_template: ожидает как аргумент шаблон конфигурации trunk-портов в виде
  списка команд (пример trunk_cmd_list)

Функция должна возвращать список команд с конфигурацией на основе указанных портов
и шаблона trunk_cmd_list. В конце строк в списке не должно быть символа
перевода строки.
Если в шаблоне trunk_template есть команда switchport trunk allowed vlan, добавить к
ней вланы указанные в словаре intf_vlan_dict.

Проверить работу функции на примере словаря trunk_dict и списка команд trunk_cmd_list.
Если предыдущая проверка прошла успешно, проверить работу функции еще раз
на словаре trunk_dict_2 и убедится, что в итоговом списке правильные номера
интерфейсов и вланов.


Пример работы функции
In [8]: generate_trunk_config(trunk_dict, trunk_cmd_list)
Out[8]:
['interface FastEthernet0/1',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 10,20,30',
 'interface FastEthernet0/2',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 11,30',
 'interface FastEthernet0/4',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 17']

In [9]: generate_trunk_config(trunk_dict_2, trunk_cmd_list)
Out[9]:
['interface FastEthernet0/11',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 120,131',
 'interface FastEthernet0/15',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 111,130',
 'interface FastEthernet0/14',
 'switchport mode trunk',
 'switchport trunk native vlan 999',
 'switchport trunk allowed vlan 117']


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""

trunk_cmd_list = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_dict = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_dict_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}
# -*- coding: utf-8 -*-
"""
Завдання 9.6a

Сделать копию функции get_int_vlan_map из задания 9.6.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt
Пример работы функции
In [2]: get_int_vlan_map("config_sw2.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30,
  'FastEthernet1/3': 1,
  'FastEthernet2/0': 1,
  'FastEthernet2/1': 1},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [4]: access, trunk = get_int_vlan_map("config_sw2.txt")

In [5]: access
Out[5]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30,
 'FastEthernet1/3': 1,
 'FastEthernet2/0': 1,
 'FastEthernet2/1': 1}

In [6]: trunk
Out[6]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
# -*- coding: utf-8 -*-
"""
Завдання 9.6

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access
  VLAN (числа)
* словарь портов в режиме trunk, где ключи номера портов, а значения список
  разрешенных VLAN (список чисел)

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Пример работы функции
In [2]: get_int_vlan_map("config_sw1.txt")
Out[2]:
({'FastEthernet0/0': 10,
  'FastEthernet0/2': 20,
  'FastEthernet1/0': 20,
  'FastEthernet1/1': 30},
 {'FastEthernet0/1': [100, 200],
  'FastEthernet0/3': [100, 300, 400, 500, 600],
  'FastEthernet1/2': [400, 500, 600]})

In [3]: access, trunk = get_int_vlan_map("config_sw1.txt")

In [4]: access
Out[4]:
{'FastEthernet0/0': 10,
 'FastEthernet0/2': 20,
 'FastEthernet1/0': 20,
 'FastEthernet1/1': 30}

In [5]: trunk
Out[5]:
{'FastEthernet0/1': [100, 200],
 'FastEthernet0/3': [100, 300, 400, 500, 600],
 'FastEthernet1/2': [400, 500, 600]}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
# -*- coding: utf-8 -*-
"""
Завдання 9.7

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный
файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (команды которые НЕ начинаются с пробела), будут ключами.
* Если у команды верхнего уровня есть подкоманды (команды которые начинаются с
  пробела), они должны быть в значении у соответствующего ключа, в виде списка
  (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются
с '!', пустые строки, а также строки в которых содержатся слова из списка ignore.

Пример работы функции:
In [3]: pprint(convert_config_to_dict("config_r2_short.txt"), sort_dicts=False)
{'version 15.2': [],
 'no service timestamps debug uptime': [],
 'no service timestamps log uptime': [],
 'hostname PE_r2': [],
 'no ip http server': [],
 'no ip http secure-server': [],
 'ip route 10.2.2.2 255.255.255.255 Tunnel0': [],
 'ip access-list standard LDP': ['deny   10.0.0.0 0.0.255.255',
                                 'permit 10.0.0.0 0.255.255.255'],
 'ip prefix-list TEST seq 5 permit 10.6.6.6/32': [],
 'mpls ldp router-id Loopback0 force': [],
 'control-plane': [],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all']}

In [4]: pprint(convert_config_to_dict("config_sw1.txt"), sort_dicts=False)
{'version 15.0': [],
 'service timestamps debug datetime msec': [],
 'service timestamps log datetime msec': [],
 'no service password-encryption': [],
 'hostname sw1': [],
 'interface FastEthernet0/0': ['switchport mode access',
                               'switchport access vlan 10'],
 'interface FastEthernet0/1': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,200',
                               'switchport mode trunk'],
 'interface FastEthernet0/2': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet0/3': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 100,300,400,500,600',
                               'switchport mode trunk'],
 'interface FastEthernet1/0': ['switchport mode access',
                               'switchport access vlan 20'],
 'interface FastEthernet1/1': ['switchport mode access',
                               'switchport access vlan 30'],
 'interface FastEthernet1/2': ['switchport trunk encapsulation dot1q',
                               'switchport trunk allowed vlan 400,500,600',
                               'switchport mode trunk'],
 'interface Vlan100': ['ip address 10.0.100.1 255.255.255.0'],
 'line con 0': ['exec-timeout 0 0',
                'privilege level 15',
                'logging synchronous'],
 'line aux 0': [],
 'line vty 0 4': ['login', 'transport input all'],
 'end': []}


В заданиях 9го раздела и дальше, кроме указанной функции можно создавать любые
дополнительные функции.
"""
ignore = ["duplex", "alias", "configuration"]
# -*- coding: utf-8 -*-
"""
Завдання 11.0

Пройти всі питання в pquiz по розділу 11.
Перед проходженням питань оновити pyneng-quiz:
$ pip install -U pyneng-quiz

Запуск:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
Завдання 11.1a

Создать функцию convert_mac_list которая конвертирует список MAC-адресов из
разных форматов в 1a:1b:2c:2d:3e:3f.

Конвертация MAC-адресов должна выполняться с помощью функции convert_mac из
задания 11.1. При этом нельзя копировать код функции convert_mac.

У функции convert_mac_list должно быть два параметра:
* mac_list - ожидает как аргумент список с MAC-адресами
* strict - параметр, который контролирует, что делать с неправильными
  MAC-адресами. Возможные значения True/False. Значение по умолчанию False.

Если все MAC-адреса правильные, функция должна вернуть список этих же
MAC-адресов, но в формате 1a:1b:2c:2d:3e:3f. Если какие-то MAC-адреса
неправильные (функция convert_mac сгенерировала исключение ValueError), в
зависимости от параметра strict надо:
* если strict равен True - не перехватывать исключение ValueError из функции
  convert_mac
* если strict равен False - игнорировать неправильные MAC-адреса и добавить в
  список только те, которые прошли проверку

Пример работы функции:

In [9]: convert_mac_list(["1a1b.2c2d.3e3f", "111122223333", "11-11-22-22-33-33"], strict=False)
Out[9]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33', '11:11:22:22:33:33']

In [10]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=False)
Out[10]: ['1a:1b:2c:2d:3e:3f', '11:11:22:22:33:33']

In [11]: convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=True)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [11], in <cell line: 1>()
----> 1 convert_mac_list(["1a1b.2c2d.3e3f", "1111WWWW3333", "11-11-22-22-33-33"], strict=True)
...
ValueError: '1111WWWW3333' does not appear to be a MAC address
"""
# -*- coding: utf-8 -*-
"""
Завдання 11.1

Создать функцию convert_mac которая конвертирует mac-адрес из разных форматов в
1a:1b:2c:2d:3e:3f.
У функции должен быть один параметр: mac_address, который ожидает строку с
MAC-адресом в одном из форматов ниже.  Функция должна возвращать строку с
MAC-адресом в формате 1a:1b:2c:2d:3e:3f.

Должна поддерживаться конвертация из таких форматов:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a1b-2c2d-3e3f
* 1a:1b:2c:2d:3e:3f (оставить без изменений)

Функция также должна проверять, что строка, которая была передана функции,
содержит правильный MAC-адрес. MAC-адрес считается правильным, если он:
- записан в одном из поддерживаемых форматов
- каждый символ, кроме разделителей ":,-.", это символ в диапазоне a-f или 0-9
- не считая разделители, в MAC-адресе должно быть 12 символов

Если как аргумент была передана строка, которая не содержит правильный
MAC-адрес, сгенерировать исключение ValueError (... должно быть заменено на
переданное значение, примеры ниже): ValueError: '...' does not appear to be a
MAC address

Проверить работу функции на разных MAC-адресах в списке mac_list.

Пример работы функции:

In [2]: convert_mac("1a1b.2c2d.3e3f")
Out[2]: '1a:1b:2c:2d:3e:3f'

In [3]: convert_mac("1111.2222.3333")
Out[3]: '11:11:22:22:33:33'

In [4]: convert_mac("111122223333")
Out[4]: '11:11:22:22:33:33'

In [5]: convert_mac("1111-2222-3333")
Out[5]: '11:11:22:22:33:33'

In [6]: convert_mac("1111-2222-33")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [6], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33")
...
ValueError: '1111-2222-33' does not appear to be a MAC address


In [7]: convert_mac("1111-2222-33WW")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Input In [7], in <cell line: 1>()
----> 1 convert_mac("1111-2222-33WW")
...
ValueError: '1111-2222-33WW' does not appear to be a MAC address

"""
"""
Завдання 11.2

Создать функцию prompt_user_ip которая запрашивает пользователя ввод IP-адреса,
проверяет правильность введенного адреса и, если он неправильный, запрашивает
адрес снова. Если пользователь ввел правильный IP-адрес, функция возвращает его.

У функции prompt_user_ip должны быть такие параметры:
* max_retry - максимальное количество попыток ввода IP-адреса. Значение по умолчанию 5.
* ensure_unicast - если параметру передано значение True, адрес должен быть не
  только правильным в целом, но и должен быть именно unicast адресом, то есть
  первый октет адреса должен быть в диапазоне 1-223.  Возможные значения
  True/False. Значение по умолчанию False.

IP-адрес считается правильным, если он:
- состоит из 4 чисел (а не букв или других символов)
- числа разделены точкой
- каждое число в диапазоне от 0 до 255


Пример работы функции:

In [7]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 10.1.1.1.1
Неправильный IP-адрес
Введите правильный IP-адрес: 10.1.1.1
Out[7]: '10.1.1.1'

In [8]: prompt_user_ip(max_retry=5, ensure_unicast=False)
Введите правильный IP-адрес: 110.1.500.1
Неправильный IP-адрес
Введите правильный IP-адрес: 4.4.4.4
Out[8]: '4.4.4.4'

In [9]: prompt_user_ip(max_retry=3, ensure_unicast=False)
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
Введите правильный IP-адрес: a
Неправильный IP-адрес
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

In [10]: prompt_user_ip(max_retry=5, ensure_unicast=True)
Введите правильный IP-адрес: 255.255.255.255
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 10.1.1.1
Out[10]: '10.1.1.1'

In [12]: prompt_user_ip(max_retry=3, ensure_unicast=True)
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
Введите правильный IP-адрес: 0.0.0.0
Введите IP-адрес в диапазоне unicast: 1-223
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: После 3 попыток не был введен правильный адрес

"""
# -*- coding: utf-8 -*-
"""
Завдання 11.3

Создать функцию parse_cdp_neighbors, которая обрабатывает вывод команды show
cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как
аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все
содержимое файла в строку, а затем передать строку как аргумент функции (как
передать вывод команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция
должна работать и на других файлах (тест проверяет работу функции на выводе из
sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Пример работы функции
In [3]: with open("sh_cdp_n_sw1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')}

In [4]: with open("sh_cdp_n_r1.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

In [5]: with open("sh_cdp_n_r2.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R2', 'Eth0/0'): ('SW1', 'Eth0/2'), ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

In [6]: with open("sh_cdp_n_r3.txt") as f:
   ...:     pprint(parse_cdp_neighbors(f.read()))
   ...:
{('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

"""

def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
# -*- coding: utf-8 -*-
"""
Завдання 11.4a

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

С помощью функции create_network_map из задания 11.4 создать словарь topology
с описанием топологии для файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему
для словаря topology, полученного с помощью create_network_map.  Как работать с
функцией draw_topology надо разобраться самостоятельно, почитав описание
функции в файле draw_network_graph.py.  Полученная схема будет записана в файл
svg - его можно открыть браузером.

С текущим словарем topology на схеме нарисованы лишние соединения. Они
возникают потому что в одном файле CDP (sh_cdp_n_r1.txt) описывается соединение
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
а в другом (sh_cdp_n_sw1.txt)
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

В этом задании надо создать новую функцию unique_network_map, которая из этих
двух соединений будет оставлять только одно, для корректного рисования схемы.
При этом все равно какое из соединений оставить.

У функции unique_network_map должен быть один параметр topology_dict, который
ожидает как аргумент словарь.  Это должен быть словарь полученный в результате
выполнения функции create_network_map из задания 11.4.

Пример словаря:
{
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
}


Функция должна возвращать словарь, который описывает соединения между
устройствами. В словаре надо избавиться от "дублирующих" соединений
и оставлять только одно из них.

Структура итогового словаря такая же, как в задании 11.4:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

После создания функции, попробовать еще раз нарисовать топологию,
теперь уже для словаря, который возвращает функция unique_network_map.

Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg

При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций create_network_map и draw_topology.

Пример работы функции
input_topology = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
}

In [7]: pprint(unique_network_map(input_topology))
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11')}

"""

infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
# -*- coding: utf-8 -*-
"""
Завдання 11.4

Создать функцию create_network_map, которая обрабатывает вывод команды show cdp
neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент
список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между
устройствами. Структура словаря такая же, как в задании 11.3:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

Не копировать код функции parse_cdp_neighbors.
Если функция parse_cdp_neighbors не может обработать вывод одного из файлов
с выводом команды, надо исправить код функции в задании 11.3.

Пример работы функции
In [3]: pprint(create_network_map(infiles), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [4]: pprint(create_network_map(["sh_cdp_n_sw1.txt", "sh_cdp_n_r1.txt"]), sort_dicts=False)
{('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
 ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
 ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
 ('SW1', 'Eth0/5'): ('R6', 'Eth0/1'),
 ('R1', 'Eth0/0'): ('SW1', 'Eth0/1')}

"""
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
# -*- coding: utf-8 -*-
"""
Завдання 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функція має повертати кортеж із двома списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через
subprocess).  IP-адрес считается доступным, если выполнение команды ping
отработало с кодом 0 (returncode).  Нюансы: на Windows returncode может быть
равен 0 не только, когда ping был успешен, но для задания нужно проверять
именно код. Это сделано для упрощения тестов.

"""
# -*- coding: utf-8 -*-
"""
Завдання 12.2

Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Пример вызова функции
In [3]: convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])
Out[3]:
['8.8.4.4',
 '1.1.1.1',
 '1.1.1.2',
 '1.1.1.3',
 '172.21.41.128',
 '172.21.41.129',
 '172.21.41.130',
 '172.21.41.131',
 '172.21.41.132']

In [4]: convert_ranges_to_ip_list(['8.8.4.4', '1.1.1.10-12', '10.1.1.1-10.1.1.4'])
Out[4]:
['8.8.4.4',
 '1.1.1.10',
 '1.1.1.11',
 '1.1.1.12',
 '10.1.1.1',
 '10.1.1.2',
 '10.1.1.3',
 '10.1.1.4']

"""
# -*- coding: utf-8 -*-
"""
Завдання 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функція нічого не повертає, только делает print.

Пример вызова функции
In [6]: reach_ip = ["10.1.1.1", "10.1.1.2"]
In [7]: unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]

In [8]: print_ip_table(reach_ip, unreach_ip)
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
