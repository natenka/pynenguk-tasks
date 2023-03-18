# -*- coding: utf-8 -*-
"""
Завдання 25.4

Для завдань 25 розділу немає тестів!

Скопіювати файл get_data із завдання 25.2.
Додати в скрипт підтримку стовпця active, який ми додали у завданні 25.3.

Тепер, при запиті інформації, спочатку мають відображатися активні записи, а
потім неактивні. Якщо неактивних записів немає, не відображати заголовок
"Inactive entries".

Приклади виконання скрипту
$ python get_data.py
The dhcp table has the following entries:

Active entries:

-----------------  ----------  --  ----------------  ---  -
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1   sw1  1
00:04:A3:3E:5B:69  10.1.15.2   15  FastEthernet0/15  sw1  1
00:05:B3:7E:9B:60  10.1.5.4     5  FastEthernet0/9   sw1  1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5   sw1  1
00:E9:BC:3F:A6:50  100.1.1.6    3  FastEthernet0/20  sw3  1
00:E9:22:11:A6:50  100.1.1.7    3  FastEthernet0/21  sw3  1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7   sw2  1
00:B4:A3:3E:5B:69  10.1.5.20    5  FastEthernet0/5   sw2  1
00:A9:BC:3F:A6:50  10.1.10.65  20  FastEthernet0/2   sw2  1
00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4   sw2  1
-----------------  ----------  --  ----------------  ---  -

Inactive entries:

-----------------  ---------------  -  ---------------  ---  -
00:09:BC:3F:A6:50  192.168.100.100  1  FastEthernet0/7  sw1  0
00:C5:B3:7E:9B:60  10.1.5.40        5  FastEthernet0/9  sw2  0
-----------------  ---------------  -  ---------------  ---  -

$ python get_data.py vlan 5

Information about devices with the following parameters: vlan 5

Active entries:

-----------------  ---------  -  ---------------  ---  -
00:05:B3:7E:9B:60  10.1.5.4   5  FastEthernet0/9  sw1  1
00:B4:A3:3E:5B:69  10.1.5.20  5  FastEthernet0/5  sw2  1
-----------------  ---------  -  ---------------  ---  -

Inactive entries:

-----------------  ---------  -  ---------------  ---  -
00:C5:B3:7E:9B:60  10.1.5.40  5  FastEthernet0/9  sw2  0
-----------------  ---------  -  ---------------  ---  -


$ python get_data.py vlan 10

Information about devices with the following parameters: vlan 10

Active entries:

-----------------  ----------  --  ---------------  ---  -
00:09:BB:3D:D6:58  10.1.10.2   10  FastEthernet0/1  sw1  1
00:07:BC:3F:A6:50  10.1.10.6   10  FastEthernet0/5  sw1  1
00:A9:BB:3D:D6:58  10.1.10.20  10  FastEthernet0/7  sw2  1
00:A9:33:44:A6:50  10.1.10.77  10  FastEthernet0/4  sw2  1
-----------------  ----------  --  ---------------  ---  -
"""
