# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.1

–û–±—Ä–∞–±–æ—Ç–∞—Ç—å —Å—Ç—Ä–æ–∫–∏ –∏–∑ —Ñ–∞–π–ª–∞ ospf.txt –∏ –≤—ã–≤–µ—Å—Ç–∏ –∏–Ω—Ñ–æ—Ä–º–∞—Ü–∏—é –ø–æ –∫–∞–∂–¥–æ–π —Å—Ç—Ä–æ–∫–µ –≤ —Ç–∞–∫–æ–º
–≤–∏–¥–µ –Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π –ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.2a

–°–æ–∑–¥–∞—Ç—å —Å–∫—Ä–∏–ø—Ç, –∫–æ—Ç–æ—Ä—ã–π –±—É–¥–µ—Ç –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞—Ç—å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏
–≤—ã–≤–æ–¥–∏—Ç—å –Ω–∞ —ç–∫—Ä–∞–Ω —Å—Ç—Ä–æ–∫–∏ –∏–∑ –∫–æ–Ω—Ñ–∏–≥–∞, –∏—Å–∫–ª—é—á–∞—è –Ω–µ–∫–æ—Ç–æ—Ä—ã–µ.

–ò–º—è —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É.
$ python task_7_2a.py config_sw1.txt

–í—ã–≤–µ—Å—Ç–∏ –Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π –ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞ –∫–æ–º–∞–Ω–¥—ã –∏–∑ –ø–µ—Ä–µ–¥–∞–Ω–Ω–æ–≥–æ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ
—Ñ–∞–π–ª–∞, –∏—Å–∫–ª—é—á–∞—è —Å—Ç—Ä–æ–∫–∏, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å '!' –∏ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ—Ç–æ—Ä—ã—Ö —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è
—Å–ª–æ–≤–∞ –∏–∑ —Å–ø–∏—Å–∫–∞ ignore.
–í—ã–≤–æ–¥ –Ω–µ –¥–æ–ª–∂–µ–Ω —Å–æ–¥–µ—Ä–∂–∞—Ç—å –ø—É—Å—Ç—ã–µ —Å—Ç—Ä–æ–∫–∏.

–ü—Ä–∏–º–µ—Ä –≤—ã–≤–æ–¥–∞:
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

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Å–∫—Ä–∏–ø—Ç–∞ –Ω–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–º —Ñ–∞–π–ª–µ config_sw1.txt.
–ò–º—è —Ñ–∞–π–ª–∞ –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É.

"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.2b

–°–∫–æ–ø–∏—Ä–æ–≤–∞—Ç—å –∫–æ–¥ –∏–∑ –∑–∞–¥–∞–Ω–∏—è 7.2a –∏ –ø–µ—Ä–µ–¥–µ–ª–∞—Ç—å –µ–≥–æ: –≤–º–µ—Å—Ç–æ –≤—ã–≤–æ–¥–∞ –Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π
–ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞, —Å–∫—Ä–∏–ø—Ç –¥–æ–ª–∂–µ–Ω –∑–∞–ø–∏—Å–∞—Ç—å –ø–æ–ª—É—á–µ–Ω–Ω—ã–µ —Å—Ç—Ä–æ–∫–∏ –≤ —Ñ–∞–π–ª.

–ò–º–µ–Ω–∞ —Ñ–∞–π–ª–æ–≤ –Ω—É–∂–Ω–æ –ø–µ—Ä–µ–¥–∞–≤–∞—Ç—å –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç—ã —Å–∫—Ä–∏–ø—Ç—É:
1 –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∏—Å—Ö–æ–¥–Ω–æ–≥–æ —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏
2 –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∏—Ç–æ–≥–æ–≤–æ–≥–æ —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏, –≤ –∫–æ—Ç–æ—Ä—ã–π –±—É–¥—É—Ç –∑–∞–ø–∏—Å–∞–Ω—ã —Å—Ç—Ä–æ–∫–∏

–ü—Ä–∏–º–µ—Ä –≤—ã–∑–æ–≤–∞:
$ python task_7_2b.py config_sw1.txt new_config.txt

–ü—Ä–∏ —ç—Ç–æ–º, –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –æ—Ç—Ñ–∏–ª—å—Ç—Ä–æ–≤–∞–Ω—ã —Å—Ç—Ä–æ–∫–∏ —Å–æ —Å–ª–æ–≤–∞–º–∏, –∫–æ—Ç–æ—Ä—ã–µ —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è –≤ —Å–ø–∏—Å–∫–µ ignore
–∏ —Å—Ç—Ä–æ–∫–∏, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è –Ω–∞ '!'.
"""

ignore = ["duplex", "alias", "configuration", "end", "service"]
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.2

–°–æ–∑–¥–∞—Ç—å —Å–∫—Ä–∏–ø—Ç, –∫–æ—Ç–æ—Ä—ã–π –±—É–¥–µ—Ç –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞—Ç—å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏
–≤—ã–≤–æ–¥–∏—Ç—å –Ω–∞ —ç–∫—Ä–∞–Ω —Å—Ç—Ä–æ–∫–∏ –∏–∑ –∫–æ–Ω—Ñ–∏–≥–∞, –∏—Å–∫–ª—é—á–∞—è –Ω–µ–∫–æ—Ç–æ—Ä—ã–µ.

–ò–º—è —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É.
$ python task_7_2.py config_sw1.txt

–í—ã–≤–µ—Å—Ç–∏ –Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π –ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞ –∫–æ–º–∞–Ω–¥—ã –∏–∑ –ø–µ—Ä–µ–¥–∞–Ω–Ω–æ–≥–æ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ
—Ñ–∞–π–ª–∞, –∏—Å–∫–ª—é—á–∞—è —Å—Ç—Ä–æ–∫–∏, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å '!'.

–í—ã–≤–æ–¥ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –±–µ–∑ –ø—É—Å—Ç—ã—Ö —Å—Ç—Ä–æ–∫.

–ü—Ä–∏–º–µ—Ä –≤—ã–≤–æ–¥–∞:
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
–ó–∞–≤–¥–∞–Ω–Ω—è 7.3a

–°–¥–µ–ª–∞—Ç—å –∫–æ–ø–∏—é —Å–∫—Ä–∏–ø—Ç–∞ –∑–∞–¥–∞–Ω–∏—è 7.3.

–ü–µ—Ä–µ–¥–µ–ª–∞—Ç—å —Å–∫—Ä–∏–ø—Ç: –û—Ç—Å–æ—Ä—Ç–∏—Ä–æ–≤–∞—Ç—å –≤—ã–≤–æ–¥ –ø–æ –Ω–æ–º–µ—Ä—É VLAN

–í —Ä–µ–∑—É–ª—å—Ç–∞—Ç–µ –¥–æ–ª–∂–µ–Ω –ø–æ–ª—É—á–∏—Ç—å—Å—è —Ç–∞–∫–æ–π –≤—ã–≤–æ–¥:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

–û–±—Ä–∞—Ç–∏—Ç–µ –≤–Ω–∏–º–∞–Ω–∏–µ –Ω–∞ vlan 1000 - –æ–Ω –¥–æ–ª–∂–µ–Ω –≤—ã–≤–æ–¥–∏—Ç—å—Å—è –ø–æ—Å–ª–µ–¥–Ω–∏–º.
–ü—Ä–∞–≤–∏–ª—å–Ω–æ–π —Å–æ—Ä—Ç–∏—Ä–æ–≤–∫–∏ –º–æ–∂–Ω–æ –¥–æ–±–∏—Ç—å—Å—è, –µ—Å–ª–∏ vlan –±—É–¥–µ—Ç —á–∏—Å–ª–æ–º, –∞ –Ω–µ —Å—Ç—Ä–æ–∫–æ–π.

–ü–æ–¥—Å–∫–∞–∑–∫–∞: –î–ª—è —Å–æ—Ä—Ç–∏—Ä–æ–≤–∫–∏ —É–¥–æ–±–Ω–æ —Å–Ω–∞—á–∞–ª–∞ —Å–æ–∑–¥–∞—Ç—å —Å–ø–∏—Å–æ–∫ —Å–ø–∏—Å–∫–æ–≤ —Ç–∞–∫–æ–≥–æ —Ç–∏–ø–∞,
–∞ –ø–æ—Ç–æ–º —Å–æ—Ä—Ç–∏—Ä–æ–≤–∞—Ç—å.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

–°–æ—Ä—Ç–∏—Ä–æ–≤–∫–∞ –¥–æ–ª–∂–Ω–∞ –±—ã—Ç—å –ø–æ –ø–µ—Ä–≤–æ–º—É —ç–ª–µ–º–µ–Ω—Ç—É (vlan), –∞ –µ—Å–ª–∏ –ø–µ—Ä–≤—ã–π —ç–ª–µ–º–µ–Ω—Ç –æ–¥–∏–Ω–∞–∫–æ–≤—ã–π,
—Ç–æ –ø–æ –≤—Ç–æ—Ä–æ–º—É. –¢–∞–∫ —Ä–∞–±–æ—Ç–∞–µ—Ç –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é —Ñ—É–Ω–∫—Ü–∏—è sorted –∏ –º–µ—Ç–æ–¥ sort, –µ—Å–ª–∏ —Å–æ—Ä—Ç–∏—Ä–æ–≤–∞—Ç—å
—Å–ø–∏—Å–æ–∫ —Å–ø–∏—Å–∫–æ–≤ –≤—ã—à–µ.

"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.3b

–°–¥–µ–ª–∞—Ç—å –∫–æ–ø–∏—é —Å–∫—Ä–∏–ø—Ç–∞ –∑–∞–¥–∞–Ω–∏—è 7.3a.

–ü–µ—Ä–µ–¥–µ–ª–∞—Ç—å —Å–∫—Ä–∏–ø—Ç:
- –ó–∞–ø—Ä–æ—Å–∏—Ç—å —É –ø–æ–ª—å–∑–æ–≤–∞—Ç–µ–ª—è –≤–≤–æ–¥ –Ω–æ–º–µ—Ä–∞ VLAN.
- –í—ã–≤–æ–¥–∏—Ç—å –∏–Ω—Ñ–æ—Ä–º–∞—Ü–∏—é —Ç–æ–ª—å–∫–æ –ø–æ —É–∫–∞–∑–∞–Ω–Ω–æ–º—É VLAN.

–ü—Ä–∏–∫–ª–∞–¥ —Ä–æ–±–æ—Ç–∏ —Å–∫—Ä–∏–ø—Ç–∞:
$ python task_7_3b.py
–í–≤–µ–¥–∏—Ç–µ –Ω–æ–º–µ—Ä –≤–ª–∞–Ω–∞: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.3

–°–∫—Ä–∏–ø—Ç –¥–æ–ª–∂–µ–Ω –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞—Ç—å –∑–∞–ø–∏—Å–∏ –≤ —Ñ–∞–π–ª–µ CAM_table.txt. –ö–∞–∂–¥–∞—è —Å—Ç—Ä–æ–∫–∞,
–≥–¥–µ –µ—Å—Ç—å MAC-–∞–¥—Ä–µ—Å, –¥–æ–ª–∂–Ω–∞ –±—ã—Ç—å –æ–±—Ä–∞–±–æ—Ç–∞–Ω–∞ —Ç–∞–∫–∏–º –æ–±—Ä–∞–∑–æ–º, —á—Ç–æ–±—ã
–Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π –ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞ –±—ã–ª–∞ –≤—ã–≤–µ–¥–µ–Ω–∞ —Ç–∞–±–ª–∏—Ü–∞ –≤–∏–¥–∞:

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
–ó–∞–≤–¥–∞–Ω–Ω—è 7.4

–°–æ–∑–¥–∞—Ç—å —Å–∫—Ä–∏–ø—Ç, –∫–æ—Ç–æ—Ä—ã–π –±—É–¥–µ—Ç –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞—Ç—å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏
–ø–æ–ª—É—á–∞—Ç—å –∏–∑ –Ω–µ–≥–æ –∏–Ω—Ñ–æ—Ä–º–∞—Ü–∏—é –æ –ø–æ—Ä—Ç–∞—Ö –≤ —Ä–µ–∂–∏–º–µ trunk –∏ –≤–ª–∞–Ω–∞—Ö, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—Å—Ç—Ä–æ–µ–Ω—ã
–Ω–∞ —ç—Ç–∏—Ö –ø–æ—Ä—Ç–∞—Ö.

–ò–º—è —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É.
$ python task_7_4.py config_trunk_sw2.txt
$ python task_7_4.py config_trunk_sw3.txt

–ü–µ—Ä–µ–¥–∞–≤–∞—Ç—å –∏–º—è —Ñ–∞–π–ª–∞ –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É. –£–∫–∞–∑–∞–Ω–Ω—ã–π –∫–æ–Ω—Ñ–∏–≥ –Ω–∞–¥–æ –æ–±—Ä–∞–±–æ—Ç–∞—Ç—å –∏
–ø–æ–ª—É—á–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å –ø–æ—Ä—Ç–æ–≤ –≤ —Ä–µ–∂–∏–º–µ trunk, –≥–¥–µ –∫–ª—é—á–∏ –Ω–æ–º–µ—Ä–∞ –ø–æ—Ä—Ç–æ–≤,
–∞ –∑–Ω–∞—á–µ–Ω–∏—è —Å–ø–∏—Å–æ–∫ —Ä–∞–∑—Ä–µ—à–µ–Ω–Ω—ã—Ö VLAN (—Å–ø–∏—Å–æ–∫ —Å—Ç—Ä–æ–∫).

–ó–∞–ø–∏—Å–∞—Ç—å –∏—Ç–æ–≥–æ–≤—ã–π —Å–ª–æ–≤–∞—Ä—å –≤ –ø–µ—Ä–µ–º–µ–Ω–Ω—É—é trunk_dict (–∏–º–µ–Ω–Ω–æ —ç—Ç–∞ –ø–µ—Ä–µ–º–µ–Ω–Ω–∞—è –±—É–¥–µ—Ç
–ø—Ä–æ–≤–µ—Ä—è—Ç—å—Å—è –≤ —Ç–µ—Å—Ç–µ). –ü–æ –∂–µ–ª–∞–Ω–∏—é –º–æ–∂–Ω–æ –≤—ã–≤–æ–¥–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å –Ω–∞ —ç–∫—Ä–∞–Ω, —Ç–µ—Å—Ç
–ø—Ä–æ–≤–µ—Ä—è–µ—Ç —Ç–æ–ª—å–∫–æ —Å–æ–¥–µ—Ä–∂–∏–º–æ–µ –ø–µ—Ä–µ–º–µ–Ω–Ω–æ–π. –¢—É—Ç —É–¥–æ–±–Ω–æ –≤—ã–≤–æ–¥–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å —Å –ø–æ–º–æ—â—å—é pprint.

–ù–∞–ø—Ä–∏–º–µ—Ä, –¥–ª—è —Ñ–∞–π–ª–∞ config_trunk_sw2.txt –¥–æ–ª–∂–µ–Ω –ø–æ–ª—É—á–∏—Ç—å—Å—è —Ç–∞–∫–æ–π —Å–ª–æ–≤–∞—Ä—å:

$ python task_7_4.py config_trunk_sw2.txt
{'FastEthernet0/1': ['100', '200'],
 'FastEthernet0/3': ['100', '300', '400', '500', '600'],
 'FastEthernet0/4': ['400', '500', '600']}

–î–ª—è —Ñ–∞–π–ª–∞ config_trunk_sw3.txt –¥–æ–ª–∂–µ–Ω –ø–æ–ª—É—á–∏—Ç—å—Å—è —Ç–∞–∫–æ–π —Å–ª–æ–≤–∞—Ä—å:
$ python task_7_4.py config_trunk_sw3.txt
{'FastEthernet0/1': ['10', '20', '21', '22'],
 'FastEthernet0/2': ['10', '13', '1450', '1451', '1452'],
 'FastEthernet0/6': ['40', '50', '60']}


–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–æ–≤ config_trunk_sw2.txt –∏ config_trunk_sw3.txt.
–£–±–µ–¥–∏—Ç—å—Å—è, —á—Ç–æ –¥–ª—è —ç—Ç–∏—Ö —Ñ–∞–π–ª–æ–≤ –ø–æ–ª—É—á–∞—é—Ç—Å—è –ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ —Å–ª–æ–≤–∞—Ä–∏.

–ü–æ–¥—Å–∫–∞–∑–∫–∞ –ø–æ —Å–∏–Ω—Ç–∞–∫—Å–∏—Å—É cisco: –≤ —ç—Ç–æ–º –∑–∞–¥–∞–Ω–∏–∏ —Å—á–∏—Ç–∞–µ–º, —á—Ç–æ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å –Ω–∞—Ö–æ–¥–∏—Ç—Å—è
–≤ —Ä–µ–∂–∏–º–µ trunk, –µ—Å–ª–∏ —É –Ω–µ–≥–æ –Ω–∞—Å—Ç—Ä–æ–µ–Ω–∞ –∫–æ–º–∞–Ω–¥–∞ switchport trunk allowed vlan.
"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 7.5

–°–æ–∑–¥–∞—Ç—å —Å–∫—Ä–∏–ø—Ç, –∫–æ—Ç–æ—Ä—ã–π –±—É–¥–µ—Ç –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞—Ç—å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏
–ø–æ–ª—É—á–∞—Ç—å –∏–∑ –Ω–µ–≥–æ –∏–Ω—Ñ–æ—Ä–º–∞—Ü–∏—é –æ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–æ–≤.

–ò–º—è —Ñ–∞–π–ª–∞ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É.
$ python task_7_5.py config_trunk_sw2.txt
$ python task_7_5.py config_trunk_sw3.txt

–ü–µ—Ä–µ–¥–∞–≤–∞—Ç—å –∏–º—è —Ñ–∞–π–ª–∞ –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–∫—Ä–∏–ø—Ç—É. –£–∫–∞–∑–∞–Ω–Ω—ã–π –∫–æ–Ω—Ñ–∏–≥ –Ω–∞–¥–æ –æ–±—Ä–∞–±–æ—Ç–∞—Ç—å –∏
–ø–æ–ª—É—á–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å –≥–¥–µ –∫–ª—é—á–∏ –∏–º—è –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–∞, –∞ –∑–Ω–∞—á–µ–Ω–∏–µ —Å–ø–∏—Å–æ–∫ –∫–æ–º–∞–Ω–¥, –∫–æ—Ç–æ—Ä—ã–µ
–Ω–∞—á–∏–Ω–∞—é—Ç—Å—è –Ω–∞ switchport. –ö–æ–º–∞–Ω–¥—ã –≤ —Å–ø–∏—Å–∫–µ –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –±–µ–∑ –ø—Ä–æ–±–µ–ª–∞ –≤ –Ω–∞—á–∞–ª–µ
—Å—Ç—Ä–æ–∫–∏ –∏ –ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ–Ω—Ü–µ.

–ó–∞–ø–∏—Å–∞—Ç—å –∏—Ç–æ–≥–æ–≤—ã–π —Å–ª–æ–≤–∞—Ä—å –≤ –ø–µ—Ä–µ–º–µ–Ω–Ω—É—é interface_dict (–∏–º–µ–Ω–Ω–æ —ç—Ç–∞ –ø–µ—Ä–µ–º–µ–Ω–Ω–∞—è –±—É–¥–µ—Ç
–ø—Ä–æ–≤–µ—Ä—è—Ç—å—Å—è –≤ —Ç–µ—Å—Ç–µ). –ü–æ –∂–µ–ª–∞–Ω–∏—é –º–æ–∂–Ω–æ –≤—ã–≤–æ–¥–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å –Ω–∞ —ç–∫—Ä–∞–Ω, —Ç–µ—Å—Ç
–ø—Ä–æ–≤–µ—Ä—è–µ—Ç —Ç–æ–ª—å–∫–æ —Å–æ–¥–µ—Ä–∂–∏–º–æ–µ –ø–µ—Ä–µ–º–µ–Ω–Ω–æ–π. –¢—É—Ç —É–¥–æ–±–Ω–æ –≤—ã–≤–æ–¥–∏—Ç—å —Å–ª–æ–≤–∞—Ä—å —Å –ø–æ–º–æ—â—å—é pprint.

–ù–∞–ø—Ä–∏–º–µ—Ä, –¥–ª—è —Ñ–∞–π–ª–∞ config_trunk_sw2.txt –¥–æ–ª–∂–µ–Ω –ø–æ–ª—É—á–∏—Ç—å—Å—è —Ç–∞–∫–æ–π —Å–ª–æ–≤–∞—Ä—å:

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

–î–ª—è —Ñ–∞–π–ª–∞ config_trunk_sw3.txt –¥–æ–ª–∂–µ–Ω –ø–æ–ª—É—á–∏—Ç—å—Å—è —Ç–∞–∫–æ–π —Å–ª–æ–≤–∞—Ä—å:
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

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–æ–≤ config_trunk_sw2.txt –∏ config_trunk_sw3.txt.
–£–±–µ–¥–∏—Ç—å—Å—è, —á—Ç–æ –¥–ª—è —ç—Ç–∏—Ö —Ñ–∞–π–ª–æ–≤ –ø–æ–ª—É—á–∞—é—Ç—Å—è –ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ —Å–ª–æ–≤–∞—Ä–∏.

"""
from pprint import pprint
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.0

–ü—Ä–æ–π—Ç–∏ –≤—Å—ñ –ø–∏—Ç–∞–Ω–Ω—è –≤ pquiz –ø–æ —Ä–æ–∑–¥—ñ–ª—É 09.
–ü–µ—Ä–µ–¥ –ø—Ä–æ—Ö–æ–¥–∂–µ–Ω–Ω—è–º –ø–∏—Ç–∞–Ω—å –æ–Ω–æ–≤–∏—Ç–∏ pyneng-quiz:
$ pip install -U pyneng-quiz

–ó–∞–ø—É—Å–∫:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.1

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é convert_mac, –∫–æ—Ç–æ—Ä–∞—è –∫–æ–Ω–≤–µ—Ä—Ç–∏—Ä—É–µ—Ç MAC-–∞–¥—Ä–µ—Å –∏–∑ —Ñ–æ—Ä–º–∞—Ç–∞
1a1b.2c2d.3e3f –≤ 1a:1b:2c:2d:3e:3f.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä: mac_address, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç —Å—Ç—Ä–æ–∫—É —Å
MAC-–∞–¥—Ä–µ—Å–æ–º –≤ —Ñ–æ—Ä–º–∞—Ç–µ 1a1b.2c2d.3e3f.  –§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å—Ç—Ä–æ–∫—É —Å
MAC-–∞–¥—Ä–µ—Å–æ–º –≤ —Ñ–æ—Ä–º–∞—Ç–µ 1a:1b:2c:2d:3e:3f.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ —Ä–∞–∑–Ω—ã—Ö MAC-–∞–¥—Ä–µ—Å–∞—Ö –≤ —Å–ø–∏—Å–∫–µ mac_list.

–í —ç—Ç–æ–º –∑–∞–¥–∞–Ω–∏–∏ –º–æ–∂–Ω–æ –Ω–µ –ø—Ä–æ–≤–µ—Ä—è—Ç—å, —á—Ç–æ MAC-–∞–¥—Ä–µ—Å, –∫–æ—Ç–æ—Ä—ã–π –ø–µ—Ä–µ–¥–∞–µ—Ç—Å—è —Ñ—É–Ω–∫—Ü–∏–∏
–∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –∑–∞–ø–∏—Å–∞–Ω –≤ —Ñ–æ—Ä–º–∞—Ç–µ "aaaa.bbbb.cccc". –≠—Ç–æ –±—É–¥–µ—Ç —Å–¥–µ–ª–∞–Ω–æ –≤ –∑–∞–¥–∞–Ω–∏–∏ 11–≥–æ
—Ä–∞–∑–¥–µ–ª–∞.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:

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

–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""

mac_list = ["1a1b.2c2d.3e3f", "aaaa.bbbb.cccc", "1111.2222.3333"]

# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.2

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é check_ip, –∫–æ—Ç–æ—Ä–∞—è –ø—Ä–æ–≤–µ—Ä—è–µ—Ç, —á—Ç–æ —Å—Ç—Ä–æ–∫–∞, –∫–æ—Ç–æ—Ä–∞—è –±—ã–ª–∞ –ø–µ—Ä–µ–¥–∞–Ω–∞ —Ñ—É–Ω–∫—Ü–∏–∏,
—Å–æ–¥–µ—Ä–∂–∏—Ç –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å.

–ê–¥—Ä–µ—Å —Å—á–∏—Ç–∞–µ—Ç—Å—è –ø—Ä–∞–≤–∏–ª—å–Ω—ã–º, –µ—Å–ª–∏ –æ–Ω:
- —Å–æ—Å—Ç–æ–∏—Ç –∏–∑ 4 —á–∏—Å–µ–ª (–∞ –Ω–µ –±—É–∫–≤ –∏–ª–∏ –¥—Ä—É–≥–∏—Ö —Å–∏–º–≤–æ–ª–æ–≤)
- —á–∏—Å–ª–∞ —Ä–∞–∑–¥–µ–ª–µ–Ω—ã —Ç–æ—á–∫–æ–π
- –∫–∞–∂–¥–æ–µ —á–∏—Å–ª–æ –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ –æ—Ç 0 –¥–æ 255

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä ip_addr, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç —Å—Ç—Ä–æ–∫—É —Å IP-–∞–¥—Ä–µ—Å–æ–º.
–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å True –µ—Å–ª–∏ –∞–¥—Ä–µ—Å –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π, False –∏–Ω–∞—á–µ.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ —Å—Ç—Ä–æ–∫–∞—Ö –≤ —Å–ø–∏—Å–∫–µ ip_list.
–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:
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

–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""

ip_list = ["10.1.1.1", "10.3.a.a", "500.1.1.1", "150.168.100.1", "62.150.240.300"]
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.3a

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é clean_config.  –§—É–Ω–∫—Ü–∏—è clean_config –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç
–∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∏ –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Å–ø–∏—Å–æ–∫ –∫–æ–º–∞–Ω–¥ –∏–∑ —É–∫–∞–∑–∞–Ω–Ω–æ–≥–æ
–∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ clean_config –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å —Ç–∞–∫–∏–µ –ø–∞—Ä–∞–º–µ—Ç—Ä—ã:
* config_filename - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞
* ignore_lines - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫ —Å—Ç—Ä–æ–∫, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞–¥–æ –∏–≥–Ω–æ—Ä–∏—Ä–æ–≤–∞—Ç—å.
  –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é None. –¢–æ –µ—Å—Ç—å –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é –Ω–∏–∫–∞–∫–∏–µ —Å—Ç—Ä–æ–∫–∏ –Ω–µ –∏–≥–Ω–æ—Ä—É—é—Ç—Å—è
* ignore_exclamation - –∫–æ–Ω—Ç—Ä–æ–ª–∏—Ä—É–µ—Ç —Ç–æ –∏–≥–Ω–æ—Ä–∏—Ä—É—é—Ç—Å—è –ª–∏ —Å—Ç—Ä–æ–∫–∏, –∫–æ—Ç–æ—Ä—ã–µ
  –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å –≤–æ—Å–∫–ª–∏—Ü–∞—Ç–µ–ª—å–Ω–æ–≥–æ –∑–Ω–∞–∫–∞. –í–æ–∑–º–æ–∂–Ω—ã–µ –∑–Ω–∞—á–µ–Ω–∏—è True/False.
  –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é True
* strip_lines - –∫–æ–Ω—Ç—Ä–æ–ª–∏—Ä—É–µ—Ç —É–¥–∞–ª–µ–Ω–∏–µ –ø—Ä–æ–±–µ–ª–∞ –≤ –Ω–∞—á–∞–ª–µ —Å—Ç—Ä–æ–∫–∏ –∏ –ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ–Ω—Ü–µ.
  True - —É–¥–∞–ª–∏—Ç—å –ø—Ä–æ–±–µ–ª—ã –≤ –Ω–∞—á–∞–ª–µ —Å—Ç—Ä–æ–∫–∏ –∏ –ø–µ—Ä–µ–≤–æ–¥ –≤ –∫–æ–Ω—Ü–µ, False - –Ω–µ —É–¥–∞–ª—è—Ç—å.
  –í–æ–∑–º–æ–∂–Ω—ã–µ –∑–Ω–∞—á–µ–Ω–∏—è True/False. –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é False
* delete_empty_lines - –∫–æ–Ω—Ç—Ä–æ–ª–∏—Ä—É–µ—Ç —É–¥–∞–ª–µ–Ω–∏–µ –ø—É—Å—Ç—ã—Ö —Å—Ç—Ä–æ–∫. True - —É–¥–∞–ª—è—Ç—å, False - –Ω–µ—Ç.
  –í–æ–∑–º–æ–∂–Ω—ã–µ –∑–Ω–∞—á–µ–Ω–∏—è True/False. –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é True

–î–ª—è —É–¥–æ–±—Å—Ç–≤–∞ –≤—Å–µ –∑–Ω–∞—á–µ–Ω–∏—è –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é –¥–ª—è –Ω–µ–æ–±—è–∑–∞—Ç–µ–ª—å–Ω—ã—Ö –ø–∞—Ä–∞–º–µ—Ç—Ä–æ–≤:
* ignore_lines - None
* ignore_exclamation - True
* delete_empty_lines - True
* strip_lines - False

–§—É–Ω–∫—Ü–∏—è clean_config –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∏ –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Å–ø–∏—Å–æ–∫
–∫–æ–º–∞–Ω–¥ –∏–∑ —É–∫–∞–∑–∞–Ω–Ω–æ–≥–æ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞:
* –µ—Å–ª–∏ –≤ –ø–∞—Ä–∞–º–µ—Ç—Ä ignore_lines –ø–µ—Ä–µ–¥–∞–Ω —Å–ø–∏—Å–æ–∫ —Å—Ç—Ä–æ–∫ - –∏—Å–∫–ª—é—á–∞—è —Å—Ç—Ä–æ–∫–∏ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏,
  –≤ –∫–æ—Ç–æ—Ä—ã—Ö —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è —Å—Ç—Ä–æ–∫–∏ –∏–∑ —Å–ø–∏—Å–∫–∞ ignore_lines.
* –µ—Å–ª–∏ ignore_exclamation —Ä–∞–≤–Ω–æ True - –∏—Å–∫–ª—é—á–∞—è —Å—Ç—Ä–æ–∫–∏ –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å '!'
* –µ—Å–ª–∏ delete_empty_lines —Ä–∞–≤–Ω–æ True - –∏—Å–∫–ª—é—á–∞—è –ø—É—Å—Ç—ã–µ —Å—Ç—Ä–æ–∫–∏
* –µ—Å–ª–∏ strip_lines —Ä–∞–≤–Ω–æ True - —Å—Ç—Ä–æ–∫–∏ –≤ —Å–ø–∏—Å–∫–µ –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –±–µ–∑ –ø—Ä–æ–±–µ–ª–æ–≤ –≤ –Ω–∞—á–∞–ª–µ
  –∏ –ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ–Ω—Ü–µ —Å—Ç—Ä–æ–∫–∏


–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.3

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é clean_config.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ clean_config –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å –¥–≤–∞ –ø–∞—Ä–∞–º–µ—Ç—Ä–∞:
* config_filename - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞
* ignore_lines - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫ —Å—Ç—Ä–æ–∫, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞–¥–æ –∏–≥–Ω–æ—Ä–∏—Ä–æ–≤–∞—Ç—å

–§—É–Ω–∫—Ü–∏—è clean_config –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π —Ñ–∞–π–ª –∏ –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Å–ø–∏—Å–æ–∫
–∫–æ–º–∞–Ω–¥ –∏–∑ —É–∫–∞–∑–∞–Ω–Ω–æ–≥–æ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞, –∏—Å–∫–ª—é—á–∞—è —Å—Ç—Ä–æ–∫–∏ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏,
–∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å '!' –∏ —Å—Ç—Ä–æ–∫–∏ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ –≤ –∫–æ—Ç–æ—Ä—ã—Ö —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è —Å—Ç—Ä–æ–∫–∏ –∏–∑
—Å–ø–∏—Å–∫–∞ ignore_lines.
–ö–æ–º–∞–Ω–¥—ã –≤ —Å–ø–∏—Å–∫–µ –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –±–µ–∑ –ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ–Ω—Ü–µ —Å—Ç—Ä–æ–∫–∏.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–∞ config_sw1.txt, config_sw2.txt,
config_r1.txt –∏ —Å–ø–∏—Å–∫–∞ ignore_list.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""

ignore_list = ["duplex", "alias exec", "Current configuration", "service"]

# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.4

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é generate_access_dict, –∫–æ—Ç–æ—Ä–∞—è –≥–µ–Ω–µ—Ä–∏—Ä—É–µ—Ç –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏—é
–¥–ª—è access-–ø–æ—Ä—Ç–æ–≤.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å –¥–≤–∞ –ø–∞—Ä–∞–º–µ—Ç—Ä–∞:
* intf_vlan_dict - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ª–æ–≤–∞—Ä—å —Å —Å–æ–æ—Ç–≤–µ—Ç—Å—Ç–≤–∏–µ–º –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å-VLAN
  (–ø—Ä–∏–º–µ—Ä access_dict)
* access_template - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫ —Å—Ç—Ä–æ–∫, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞–¥–æ –¥–æ–±–∞–≤–∏—Ç—å
  –¥–ª—è –∫–∞–∂–¥–æ–≥–æ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å—ã (–ø—Ä–∏–º–µ—Ä cmd_list)

–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å–ø–∏—Å–æ–∫ –≤—Å–µ—Ö –ø–æ—Ä—Ç–æ–≤ –≤ —Ä–µ–∂–∏–º–µ access —Å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–µ–π
–Ω–∞ –æ—Å–Ω–æ–≤–µ —à–∞–±–ª–æ–Ω–∞ access_cmd_list. –í –∫–æ–Ω—Ü–µ —Å—Ç—Ä–æ–∫ –≤ —Å–ø–∏—Å–∫–µ –Ω–µ –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å
—Å–∏–º–≤–æ–ª–∞ –ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏.
–ï—Å–ª–∏ –≤ —à–∞–±–ª–æ–Ω–µ access_template –µ—Å—Ç—å –∫–æ–º–∞–Ω–¥–∞ switchport access vlan, –¥–æ–±–∞–≤–∏—Ç—å –∫
–Ω–µ–π –Ω–æ–º–µ—Ä –≤–ª–∞–Ω–∞ —É–∫–∞–∑–∞–Ω–Ω—ã–π –≤ —Å–ª–æ–≤–∞—Ä–µ intf_vlan_dict

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Å–ª–æ–≤–∞—Ä—è access_dict –∏ —Å–ø–∏—Å–∫–∞ –∫–æ–º–∞–Ω–¥
access_cmd_list.  –ï—Å–ª–∏ –ø—Ä–µ–¥—ã–¥—É—â–∞—è –ø—Ä–æ–≤–µ—Ä–∫–∞ –ø—Ä–æ—à–ª–∞ —É—Å–ø–µ—à–Ω–æ, –ø—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É
—Ñ—É–Ω–∫—Ü–∏–∏ –µ—â–µ —Ä–∞–∑ –Ω–∞ —Å–ª–æ–≤–∞—Ä–µ access_dict_2 –∏ —Å–ø–∏—Å–∫–µ –∫–æ–º–∞–Ω–¥ cmd_list –∏ —É–±–µ–¥–∏—Ç—å—Å—è,
—á—Ç–æ –≤ –∏—Ç–æ–≥–æ–≤–æ–º —Å–ø–∏—Å–∫–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ –Ω–æ–º–µ—Ä–∞ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–æ–≤ –∏ –≤–ª–∞–Ω–æ–≤.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏

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


–û–≥—Ä–∞–Ω–∏—á–µ–Ω–∏–µ: –í—Å–µ –∑–∞–¥–∞–Ω–∏—è –Ω–∞–¥–æ –≤—ã–ø–æ–ª–Ω—è—Ç—å –∏—Å–ø–æ–ª—å–∑—É—è —Ç–æ–ª—å–∫–æ –ø—Ä–æ–π–¥–µ–Ω–Ω—ã–µ —Ç–µ–º—ã.

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
–ó–∞–≤–¥–∞–Ω–Ω—è 9.5a

–°–¥–µ–ª–∞—Ç—å –∫–æ–ø–∏—é —Ñ—É–Ω–∫—Ü–∏–∏ generate_trunk_config –∏–∑ –∑–∞–¥–∞–Ω–∏—è 9.5

–ò–∑–º–µ–Ω–∏—Ç—å —Ñ—É–Ω–∫—Ü–∏—é —Ç–∞–∫–∏–º –æ–±—Ä–∞–∑–æ–º, —á—Ç–æ–±—ã –æ–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞–ª–∞ –Ω–µ —Å–ø–∏—Å–æ–∫ –∫–æ–º–∞–Ω–¥, –∞ —Å–ª–æ–≤–∞—Ä—å:
- –∫–ª—é—á–∏: –∏–º–µ–Ω–∞ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–æ–≤, –≤–∏–¥–∞ 'FastEthernet0/1'
- –∑–Ω–∞—á–µ–Ω–∏—è: —Å–ø–∏—Å–æ–∫ –∫–æ–º–∞–Ω–¥, –∫–æ—Ç–æ—Ä—ã–π –Ω–∞–¥–æ –≤—ã–ø–æ–ª–Ω–∏—Ç—å –Ω–∞ —ç—Ç–æ–º –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–µ

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Å–ª–æ–≤–∞—Ä—è trunk_dict –∏ —à–∞–±–ª–æ–Ω–∞ trunk_cmd_list.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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

–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
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
–ó–∞–≤–¥–∞–Ω–Ω—è 9.5

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é generate_trunk_config, –∫–æ—Ç–æ—Ä–∞—è –≥–µ–Ω–µ—Ä–∏—Ä—É–µ—Ç
–∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏—é –¥–ª—è trunk-–ø–æ—Ä—Ç–æ–≤.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å —Ç–∞–∫–∏–µ –ø–∞—Ä–∞–º–µ—Ç—Ä—ã:

- intf_vlan_dict: –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ª–æ–≤–∞—Ä—å —Å —Å–æ–æ—Ç–≤–µ—Ç—Å—Ç–≤–∏–µ–º –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å-VLAN—ã
  (–ø—Ä–∏–º–µ—Ä trunk_dict)
- trunk_template: –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —à–∞–±–ª–æ–Ω –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏ trunk-–ø–æ—Ä—Ç–æ–≤ –≤ –≤–∏–¥–µ
  —Å–ø–∏—Å–∫–∞ –∫–æ–º–∞–Ω–¥ (–ø—Ä–∏–º–µ—Ä trunk_cmd_list)

–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å–ø–∏—Å–æ–∫ –∫–æ–º–∞–Ω–¥ —Å –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–µ–π –Ω–∞ –æ—Å–Ω–æ–≤–µ —É–∫–∞–∑–∞–Ω–Ω—ã—Ö –ø–æ—Ä—Ç–æ–≤
–∏ —à–∞–±–ª–æ–Ω–∞ trunk_cmd_list. –í –∫–æ–Ω—Ü–µ —Å—Ç—Ä–æ–∫ –≤ —Å–ø–∏—Å–∫–µ –Ω–µ –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å —Å–∏–º–≤–æ–ª–∞
–ø–µ—Ä–µ–≤–æ–¥–∞ —Å—Ç—Ä–æ–∫–∏.
–ï—Å–ª–∏ –≤ —à–∞–±–ª–æ–Ω–µ trunk_template –µ—Å—Ç—å –∫–æ–º–∞–Ω–¥–∞ switchport trunk allowed vlan, –¥–æ–±–∞–≤–∏—Ç—å –∫
–Ω–µ–π –≤–ª–∞–Ω—ã —É–∫–∞–∑–∞–Ω–Ω—ã–µ –≤ —Å–ª–æ–≤–∞—Ä–µ intf_vlan_dict.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Å–ª–æ–≤–∞—Ä—è trunk_dict –∏ —Å–ø–∏—Å–∫–∞ –∫–æ–º–∞–Ω–¥ trunk_cmd_list.
–ï—Å–ª–∏ –ø—Ä–µ–¥—ã–¥—É—â–∞—è –ø—Ä–æ–≤–µ—Ä–∫–∞ –ø—Ä–æ—à–ª–∞ —É—Å–ø–µ—à–Ω–æ, –ø—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –µ—â–µ —Ä–∞–∑
–Ω–∞ —Å–ª–æ–≤–∞—Ä–µ trunk_dict_2 –∏ —É–±–µ–¥–∏—Ç—Å—è, —á—Ç–æ –≤ –∏—Ç–æ–≥–æ–≤–æ–º —Å–ø–∏—Å–∫–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ –Ω–æ–º–µ—Ä–∞
–∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å–æ–≤ –∏ –≤–ª–∞–Ω–æ–≤.


–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
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
–ó–∞–≤–¥–∞–Ω–Ω—è 9.6a

–°–¥–µ–ª–∞—Ç—å –∫–æ–ø–∏—é —Ñ—É–Ω–∫—Ü–∏–∏ get_int_vlan_map –∏–∑ –∑–∞–¥–∞–Ω–∏—è 9.6.

–î–æ–ø–æ–ª–Ω–∏—Ç—å —Ñ—É–Ω–∫—Ü–∏—é: –¥–æ–±–∞–≤–∏—Ç—å –ø–æ–¥–¥–µ—Ä–∂–∫—É –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–∏, –∫–æ–≥–¥–∞ –Ω–∞—Å—Ç—Ä–æ–π–∫–∞ access-–ø–æ—Ä—Ç–∞
–≤—ã–≥–ª—è–¥–∏—Ç —Ç–∞–∫:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

–¢–æ –µ—Å—Ç—å, –ø–æ—Ä—Ç –Ω–∞—Ö–æ–¥–∏—Ç—Å—è –≤ VLAN 1

–í —Ç–∞–∫–æ–º —Å–ª—É—á–∞–µ, –≤ —Å–ª–æ–≤–∞—Ä—å –ø–æ—Ä—Ç–æ–≤ –¥–æ–ª–∂–Ω–∞ –¥–æ–±–∞–≤–ª—è—Ç—å—Å—è –∏–Ω—Ñ–æ—Ä–º–∞—Ü–∏—è, —á—Ç–æ –ø–æ—Ä—Ç –≤ VLAN 1
–ü—Ä–∏–º–µ—Ä —Å–ª–æ–≤–∞—Ä—è:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä config_filename, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç
–∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–∞ config_sw2.txt
–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.6

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é get_int_vlan_map, –∫–æ—Ç–æ—Ä–∞—è –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π
—Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏ –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç –∫–æ—Ä—Ç–µ–∂ –∏–∑ –¥–≤—É—Ö —Å–ª–æ–≤–∞—Ä–µ–π:
* —Å–ª–æ–≤–∞—Ä—å –ø–æ—Ä—Ç–æ–≤ –≤ —Ä–µ–∂–∏–º–µ access, –≥–¥–µ –∫–ª—é—á–∏ –Ω–æ–º–µ—Ä–∞ –ø–æ—Ä—Ç–æ–≤, –∞ –∑–Ω–∞—á–µ–Ω–∏—è access
  VLAN (—á–∏—Å–ª–∞)
* —Å–ª–æ–≤–∞—Ä—å –ø–æ—Ä—Ç–æ–≤ –≤ —Ä–µ–∂–∏–º–µ trunk, –≥–¥–µ –∫–ª—é—á–∏ –Ω–æ–º–µ—Ä–∞ –ø–æ—Ä—Ç–æ–≤, –∞ –∑–Ω–∞—á–µ–Ω–∏—è —Å–ø–∏—Å–æ–∫
  —Ä–∞–∑—Ä–µ—à–µ–Ω–Ω—ã—Ö VLAN (—Å–ø–∏—Å–æ–∫ —á–∏—Å–µ–ª)

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä config_filename, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç
–∏–º—è –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–∞ config_sw1.txt

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 9.7

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é convert_config_to_dict, –∫–æ—Ç–æ—Ä–∞—è –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω—ã–π
—Ñ–∞–π–ª –∫–æ–º–º—É—Ç–∞—Ç–æ—Ä–∞ –∏ –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Å–ª–æ–≤–∞—Ä—å:
* –í—Å–µ –∫–æ–º–∞–Ω–¥—ã –≤–µ—Ä—Ö–Ω–µ–≥–æ —É—Ä–æ–≤–Ω—è (–∫–æ–º–∞–Ω–¥—ã –∫–æ—Ç–æ—Ä—ã–µ –ù–ï –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å –ø—Ä–æ–±–µ–ª–∞), –±—É–¥—É—Ç –∫–ª—é—á–∞–º–∏.
* –ï—Å–ª–∏ —É –∫–æ–º–∞–Ω–¥—ã –≤–µ—Ä—Ö–Ω–µ–≥–æ —É—Ä–æ–≤–Ω—è –µ—Å—Ç—å –ø–æ–¥–∫–æ–º–∞–Ω–¥—ã (–∫–æ–º–∞–Ω–¥—ã –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è —Å
  –ø—Ä–æ–±–µ–ª–∞), –æ–Ω–∏ –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –≤ –∑–Ω–∞—á–µ–Ω–∏–∏ —É —Å–æ–æ—Ç–≤–µ—Ç—Å—Ç–≤—É—é—â–µ–≥–æ –∫–ª—é—á–∞, –≤ –≤–∏–¥–µ —Å–ø–∏—Å–∫–∞
  (–ø—Ä–æ–±–µ–ª—ã –≤ –Ω–∞—á–∞–ª–µ —Å—Ç—Ä–æ–∫–∏ –Ω–∞–¥–æ —É–¥–∞–ª–∏—Ç—å).
* –ï—Å–ª–∏ —É –∫–æ–º–∞–Ω–¥—ã –≤–µ—Ä—Ö–Ω–µ–≥–æ —É—Ä–æ–≤–Ω—è –Ω–µ—Ç –ø–æ–¥–∫–æ–º–∞–Ω–¥, —Ç–æ –∑–Ω–∞—á–µ–Ω–∏–µ –±—É–¥–µ—Ç –ø—É—Å—Ç—ã–º —Å–ø–∏—Å–∫–æ–º

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä config_filename, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç
–∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –∏–º—è –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –ø—Ä–∏–º–µ—Ä–µ —Ñ–∞–π–ª–∞ config_sw1.txt

–ü—Ä–∏ –æ–±—Ä–∞–±–æ—Ç–∫–µ –∫–æ–Ω—Ñ–∏–≥—É—Ä–∞—Ü–∏–æ–Ω–Ω–æ–≥–æ —Ñ–∞–π–ª–∞, –Ω–∞–¥–æ –∏–≥–Ω–æ—Ä–∏—Ä–æ–≤–∞—Ç—å —Å—Ç—Ä–æ–∫–∏, –∫–æ—Ç–æ—Ä—ã–µ –Ω–∞—á–∏–Ω–∞—é—Ç—Å—è
—Å '!', –ø—É—Å—Ç—ã–µ —Å—Ç—Ä–æ–∫–∏, –∞ —Ç–∞–∫–∂–µ —Å—Ç—Ä–æ–∫–∏ –≤ –∫–æ—Ç–æ—Ä—ã—Ö —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è —Å–ª–æ–≤–∞ –∏–∑ —Å–ø–∏—Å–∫–∞ ignore.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:
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


–í –∑–∞–¥–∞–Ω–∏—è—Ö 9–≥–æ —Ä–∞–∑–¥–µ–ª–∞ –∏ –¥–∞–ª—å—à–µ, –∫—Ä–æ–º–µ —É–∫–∞–∑–∞–Ω–Ω–æ–π —Ñ—É–Ω–∫—Ü–∏–∏ –º–æ–∂–Ω–æ —Å–æ–∑–¥–∞–≤–∞—Ç—å –ª—é–±—ã–µ
–¥–æ–ø–æ–ª–Ω–∏—Ç–µ–ª—å–Ω—ã–µ —Ñ—É–Ω–∫—Ü–∏–∏.
"""
ignore = ["duplex", "alias", "configuration"]
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 11.0

–ü—Ä–æ–π—Ç–∏ –≤—Å—ñ –ø–∏—Ç–∞–Ω–Ω—è –≤ pquiz –ø–æ —Ä–æ–∑–¥—ñ–ª—É 11.
–ü–µ—Ä–µ–¥ –ø—Ä–æ—Ö–æ–¥–∂–µ–Ω–Ω—è–º –ø–∏—Ç–∞–Ω—å –æ–Ω–æ–≤–∏—Ç–∏ pyneng-quiz:
$ pip install -U pyneng-quiz

–ó–∞–ø—É—Å–∫:
$ pquiz
"""

# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 11.1a

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é convert_mac_list –∫–æ—Ç–æ—Ä–∞—è –∫–æ–Ω–≤–µ—Ä—Ç–∏—Ä—É–µ—Ç —Å–ø–∏—Å–æ–∫ MAC-–∞–¥—Ä–µ—Å–æ–≤ –∏–∑
—Ä–∞–∑–Ω—ã—Ö —Ñ–æ—Ä–º–∞—Ç–æ–≤ –≤ 1a:1b:2c:2d:3e:3f.

–ö–æ–Ω–≤–µ—Ä—Ç–∞—Ü–∏—è MAC-–∞–¥—Ä–µ—Å–æ–≤ –¥–æ–ª–∂–Ω–∞ –≤—ã–ø–æ–ª–Ω—è—Ç—å—Å—è —Å –ø–æ–º–æ—â—å—é —Ñ—É–Ω–∫—Ü–∏–∏ convert_mac –∏–∑
–∑–∞–¥–∞–Ω–∏—è 11.1. –ü—Ä–∏ —ç—Ç–æ–º –Ω–µ–ª—å–∑—è –∫–æ–ø–∏—Ä–æ–≤–∞—Ç—å –∫–æ–¥ —Ñ—É–Ω–∫—Ü–∏–∏ convert_mac.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ convert_mac_list –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å –¥–≤–∞ –ø–∞—Ä–∞–º–µ—Ç—Ä–∞:
* mac_list - –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫ —Å MAC-–∞–¥—Ä–µ—Å–∞–º–∏
* strict - –ø–∞—Ä–∞–º–µ—Ç—Ä, –∫–æ—Ç–æ—Ä—ã–π –∫–æ–Ω—Ç—Ä–æ–ª–∏—Ä—É–µ—Ç, —á—Ç–æ –¥–µ–ª–∞—Ç—å —Å –Ω–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–º–∏
  MAC-–∞–¥—Ä–µ—Å–∞–º–∏. –í–æ–∑–º–æ–∂–Ω—ã–µ –∑–Ω–∞—á–µ–Ω–∏—è True/False. –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é False.

–ï—Å–ª–∏ –≤—Å–µ MAC-–∞–¥—Ä–µ—Å–∞ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ, —Ñ—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–µ—Ä–Ω—É—Ç—å —Å–ø–∏—Å–æ–∫ —ç—Ç–∏—Ö –∂–µ
MAC-–∞–¥—Ä–µ—Å–æ–≤, –Ω–æ –≤ —Ñ–æ—Ä–º–∞—Ç–µ 1a:1b:2c:2d:3e:3f. –ï—Å–ª–∏ –∫–∞–∫–∏–µ-—Ç–æ MAC-–∞–¥—Ä–µ—Å–∞
–Ω–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ (—Ñ—É–Ω–∫—Ü–∏—è convert_mac —Å–≥–µ–Ω–µ—Ä–∏—Ä–æ–≤–∞–ª–∞ –∏—Å–∫–ª—é—á–µ–Ω–∏–µ ValueError), –≤
–∑–∞–≤–∏—Å–∏–º–æ—Å—Ç–∏ –æ—Ç –ø–∞—Ä–∞–º–µ—Ç—Ä–∞ strict –Ω–∞–¥–æ:
* –µ—Å–ª–∏ strict —Ä–∞–≤–µ–Ω True - –Ω–µ –ø–µ—Ä–µ—Ö–≤–∞—Ç—ã–≤–∞—Ç—å –∏—Å–∫–ª—é—á–µ–Ω–∏–µ ValueError –∏–∑ —Ñ—É–Ω–∫—Ü–∏–∏
  convert_mac
* –µ—Å–ª–∏ strict —Ä–∞–≤–µ–Ω False - –∏–≥–Ω–æ—Ä–∏—Ä–æ–≤–∞—Ç—å –Ω–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–µ MAC-–∞–¥—Ä–µ—Å–∞ –∏ –¥–æ–±–∞–≤–∏—Ç—å –≤
  —Å–ø–∏—Å–æ–∫ —Ç–æ–ª—å–∫–æ —Ç–µ, –∫–æ—Ç–æ—Ä—ã–µ –ø—Ä–æ—à–ª–∏ –ø—Ä–æ–≤–µ—Ä–∫—É

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:

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
–ó–∞–≤–¥–∞–Ω–Ω—è 11.1

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é convert_mac –∫–æ—Ç–æ—Ä–∞—è –∫–æ–Ω–≤–µ—Ä—Ç–∏—Ä—É–µ—Ç mac-–∞–¥—Ä–µ—Å –∏–∑ —Ä–∞–∑–Ω—ã—Ö —Ñ–æ—Ä–º–∞—Ç–æ–≤ –≤
1a:1b:2c:2d:3e:3f.
–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä: mac_address, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç —Å—Ç—Ä–æ–∫—É —Å
MAC-–∞–¥—Ä–µ—Å–æ–º –≤ –æ–¥–Ω–æ–º –∏–∑ —Ñ–æ—Ä–º–∞—Ç–æ–≤ –Ω–∏–∂–µ.  –§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å—Ç—Ä–æ–∫—É —Å
MAC-–∞–¥—Ä–µ—Å–æ–º –≤ —Ñ–æ—Ä–º–∞—Ç–µ 1a:1b:2c:2d:3e:3f.

–î–æ–ª–∂–Ω–∞ –ø–æ–¥–¥–µ—Ä–∂–∏–≤–∞—Ç—å—Å—è –∫–æ–Ω–≤–µ—Ä—Ç–∞—Ü–∏—è –∏–∑ —Ç–∞–∫–∏—Ö —Ñ–æ—Ä–º–∞—Ç–æ–≤:
* 1a1b2c2d3e3f
* 1a1b:2c2d:3e3f
* 1a1b.2c2d.3e3f
* 1a-1b-2c-2d-3e-3f
* 1a.1b.2c.2d.3e.3f
* 1a1b-2c2d-3e3f
* 1a:1b:2c:2d:3e:3f (–æ—Å—Ç–∞–≤–∏—Ç—å –±–µ–∑ –∏–∑–º–µ–Ω–µ–Ω–∏–π)

–§—É–Ω–∫—Ü–∏—è —Ç–∞–∫–∂–µ –¥–æ–ª–∂–Ω–∞ –ø—Ä–æ–≤–µ—Ä—è—Ç—å, —á—Ç–æ —Å—Ç—Ä–æ–∫–∞, –∫–æ—Ç–æ—Ä–∞—è –±—ã–ª–∞ –ø–µ—Ä–µ–¥–∞–Ω–∞ —Ñ—É–Ω–∫—Ü–∏–∏,
—Å–æ–¥–µ—Ä–∂–∏—Ç –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π MAC-–∞–¥—Ä–µ—Å. MAC-–∞–¥—Ä–µ—Å —Å—á–∏—Ç–∞–µ—Ç—Å—è –ø—Ä–∞–≤–∏–ª—å–Ω—ã–º, –µ—Å–ª–∏ –æ–Ω:
- –∑–∞–ø–∏—Å–∞–Ω –≤ –æ–¥–Ω–æ–º –∏–∑ –ø–æ–¥–¥–µ—Ä–∂–∏–≤–∞–µ–º—ã—Ö —Ñ–æ—Ä–º–∞—Ç–æ–≤
- –∫–∞–∂–¥—ã–π —Å–∏–º–≤–æ–ª, –∫—Ä–æ–º–µ —Ä–∞–∑–¥–µ–ª–∏—Ç–µ–ª–µ–π ":,-.", —ç—Ç–æ —Å–∏–º–≤–æ–ª –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ a-f –∏–ª–∏ 0-9
- –Ω–µ —Å—á–∏—Ç–∞—è —Ä–∞–∑–¥–µ–ª–∏—Ç–µ–ª–∏, –≤ MAC-–∞–¥—Ä–µ—Å–µ –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å 12 —Å–∏–º–≤–æ–ª–æ–≤

–ï—Å–ª–∏ –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –±—ã–ª–∞ –ø–µ—Ä–µ–¥–∞–Ω–∞ —Å—Ç—Ä–æ–∫–∞, –∫–æ—Ç–æ—Ä–∞—è –Ω–µ —Å–æ–¥–µ—Ä–∂–∏—Ç –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π
MAC-–∞–¥—Ä–µ—Å, —Å–≥–µ–Ω–µ—Ä–∏—Ä–æ–≤–∞—Ç—å –∏—Å–∫–ª—é—á–µ–Ω–∏–µ ValueError (... –¥–æ–ª–∂–Ω–æ –±—ã—Ç—å –∑–∞–º–µ–Ω–µ–Ω–æ –Ω–∞
–ø–µ—Ä–µ–¥–∞–Ω–Ω–æ–µ –∑–Ω–∞—á–µ–Ω–∏–µ, –ø—Ä–∏–º–µ—Ä—ã –Ω–∏–∂–µ): ValueError: '...' does not appear to be a
MAC address

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ —Ä–∞–∑–Ω—ã—Ö MAC-–∞–¥—Ä–µ—Å–∞—Ö –≤ —Å–ø–∏—Å–∫–µ mac_list.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:

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
–ó–∞–≤–¥–∞–Ω–Ω—è 11.2

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é prompt_user_ip –∫–æ—Ç–æ—Ä–∞—è –∑–∞–ø—Ä–∞—à–∏–≤–∞–µ—Ç –ø–æ–ª—å–∑–æ–≤–∞—Ç–µ–ª—è –≤–≤–æ–¥ IP-–∞–¥—Ä–µ—Å–∞,
–ø—Ä–æ–≤–µ—Ä—è–µ—Ç –ø—Ä–∞–≤–∏–ª—å–Ω–æ—Å—Ç—å –≤–≤–µ–¥–µ–Ω–Ω–æ–≥–æ –∞–¥—Ä–µ—Å–∞ –∏, –µ—Å–ª–∏ –æ–Ω –Ω–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π, –∑–∞–ø—Ä–∞—à–∏–≤–∞–µ—Ç
–∞–¥—Ä–µ—Å —Å–Ω–æ–≤–∞. –ï—Å–ª–∏ –ø–æ–ª—å–∑–æ–≤–∞—Ç–µ–ª—å –≤–≤–µ–ª –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å, —Ñ—É–Ω–∫—Ü–∏—è –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç –µ–≥–æ.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ prompt_user_ip –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å —Ç–∞–∫–∏–µ –ø–∞—Ä–∞–º–µ—Ç—Ä—ã:
* max_retry - –º–∞–∫—Å–∏–º–∞–ª—å–Ω–æ–µ –∫–æ–ª–∏—á–µ—Å—Ç–≤–æ –ø–æ–ø—ã—Ç–æ–∫ –≤–≤–æ–¥–∞ IP-–∞–¥—Ä–µ—Å–∞. –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é 5.
* ensure_unicast - –µ—Å–ª–∏ –ø–∞—Ä–∞–º–µ—Ç—Ä—É –ø–µ—Ä–µ–¥–∞–Ω–æ –∑–Ω–∞—á–µ–Ω–∏–µ True, –∞–¥—Ä–µ—Å –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –Ω–µ
  —Ç–æ–ª—å–∫–æ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–º –≤ —Ü–µ–ª–æ–º, –Ω–æ –∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –∏–º–µ–Ω–Ω–æ unicast –∞–¥—Ä–µ—Å–æ–º, —Ç–æ –µ—Å—Ç—å
  –ø–µ—Ä–≤—ã–π –æ–∫—Ç–µ—Ç –∞–¥—Ä–µ—Å–∞ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ 1-223.  –í–æ–∑–º–æ–∂–Ω—ã–µ –∑–Ω–∞—á–µ–Ω–∏—è
  True/False. –ó–Ω–∞—á–µ–Ω–∏–µ –ø–æ —É–º–æ–ª—á–∞–Ω–∏—é False.

IP-–∞–¥—Ä–µ—Å —Å—á–∏—Ç–∞–µ—Ç—Å—è –ø—Ä–∞–≤–∏–ª—å–Ω—ã–º, –µ—Å–ª–∏ –æ–Ω:
- —Å–æ—Å—Ç–æ–∏—Ç –∏–∑ 4 —á–∏—Å–µ–ª (–∞ –Ω–µ –±—É–∫–≤ –∏–ª–∏ –¥—Ä—É–≥–∏—Ö —Å–∏–º–≤–æ–ª–æ–≤)
- —á–∏—Å–ª–∞ —Ä–∞–∑–¥–µ–ª–µ–Ω—ã —Ç–æ—á–∫–æ–π
- –∫–∞–∂–¥–æ–µ —á–∏—Å–ª–æ –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ –æ—Ç 0 –¥–æ 255


–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏:

In [7]: prompt_user_ip(max_retry=5, ensure_unicast=False)
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 10.1.1.1.1
–ù–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 10.1.1.1
Out[7]: '10.1.1.1'

In [8]: prompt_user_ip(max_retry=5, ensure_unicast=False)
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 110.1.500.1
–ù–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 4.4.4.4
Out[8]: '4.4.4.4'

In [9]: prompt_user_ip(max_retry=3, ensure_unicast=False)
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: a
–ù–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: a
–ù–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: a
–ù–µ–ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: –ü–æ—Å–ª–µ 3 –ø–æ–ø—ã—Ç–æ–∫ –Ω–µ –±—ã–ª –≤–≤–µ–¥–µ–Ω –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π –∞–¥—Ä–µ—Å

In [10]: prompt_user_ip(max_retry=5, ensure_unicast=True)
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 255.255.255.255
–í–≤–µ–¥–∏—Ç–µ IP-–∞–¥—Ä–µ—Å –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ unicast: 1-223
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 10.1.1.1
Out[10]: '10.1.1.1'

In [12]: prompt_user_ip(max_retry=3, ensure_unicast=True)
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 0.0.0.0
–í–≤–µ–¥–∏—Ç–µ IP-–∞–¥—Ä–µ—Å –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ unicast: 1-223
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 0.0.0.0
–í–≤–µ–¥–∏—Ç–µ IP-–∞–¥—Ä–µ—Å –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ unicast: 1-223
–í–≤–µ–¥–∏—Ç–µ –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π IP-–∞–¥—Ä–µ—Å: 0.0.0.0
–í–≤–µ–¥–∏—Ç–µ IP-–∞–¥—Ä–µ—Å –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ unicast: 1-223
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
...
ValueError: –ü–æ—Å–ª–µ 3 –ø–æ–ø—ã—Ç–æ–∫ –Ω–µ –±—ã–ª –≤–≤–µ–¥–µ–Ω –ø—Ä–∞–≤–∏–ª—å–Ω—ã–π –∞–¥—Ä–µ—Å

"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 11.3

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é parse_cdp_neighbors, –∫–æ—Ç–æ—Ä–∞—è –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã show
cdp neighbors.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä command_output, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫
–∞—Ä–≥—É–º–µ–Ω—Ç –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã –æ–¥–Ω–æ–π —Å—Ç—Ä–æ–∫–æ–π (–Ω–µ –∏–º—è —Ñ–∞–π–ª–∞). –î–ª—è —ç—Ç–æ–≥–æ –Ω–∞–¥–æ —Å—á–∏—Ç–∞—Ç—å –≤—Å–µ
—Å–æ–¥–µ—Ä–∂–∏–º–æ–µ —Ñ–∞–π–ª–∞ –≤ —Å—Ç—Ä–æ–∫—É, –∞ –∑–∞—Ç–µ–º –ø–µ—Ä–µ–¥–∞—Ç—å —Å—Ç—Ä–æ–∫—É –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Ñ—É–Ω–∫—Ü–∏–∏ (–∫–∞–∫
–ø–µ—Ä–µ–¥–∞—Ç—å –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã –ø–æ–∫–∞–∑–∞–Ω–æ –≤ –∫–æ–¥–µ –Ω–∏–∂–µ).

–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å–ª–æ–≤–∞—Ä—å, –∫–æ—Ç–æ—Ä—ã–π –æ–ø–∏—Å—ã–≤–∞–µ—Ç —Å–æ–µ–¥–∏–Ω–µ–Ω–∏—è –º–µ–∂–¥—É —É—Å—Ç—Ä–æ–π—Å—Ç–≤–∞–º–∏.

–ù–∞–ø—Ä–∏–º–µ—Ä, –µ—Å–ª–∏ –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –±—ã–ª –ø–µ—Ä–µ–¥–∞–Ω —Ç–∞–∫–æ–π –≤—ã–≤–æ–¥:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–µ—Ä–Ω—É—Ç—å —Ç–∞–∫–æ–π —Å–ª–æ–≤–∞—Ä—å:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

–í —Å–ª–æ–≤–∞—Ä–µ –∏–Ω—Ç–µ—Ä—Ñ–µ–π—Å—ã –¥–æ–ª–∂–Ω—ã –±—ã—Ç—å –∑–∞–ø–∏—Å–∞–Ω—ã –±–µ–∑ –ø—Ä–æ–±–µ–ª–∞ –º–µ–∂–¥—É —Ç–∏–ø–æ–º –∏ –∏–º–µ–Ω–µ–º.
–¢–æ –µ—Å—Ç—å —Ç–∞–∫ Fa0/0, –∞ –Ω–µ —Ç–∞–∫ Fa 0/0.

–ü—Ä–æ–≤–µ—Ä–∏—Ç—å —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ —Å–æ–¥–µ—Ä–∂–∏–º–æ–º —Ñ–∞–π–ª–∞ sh_cdp_n_sw1.txt. –ü—Ä–∏ —ç—Ç–æ–º —Ñ—É–Ω–∫—Ü–∏—è
–¥–æ–ª–∂–Ω–∞ —Ä–∞–±–æ—Ç–∞—Ç—å –∏ –Ω–∞ –¥—Ä—É–≥–∏—Ö —Ñ–∞–π–ª–∞—Ö (—Ç–µ—Å—Ç –ø—Ä–æ–≤–µ—Ä—è–µ—Ç —Ä–∞–±–æ—Ç—É —Ñ—É–Ω–∫—Ü–∏–∏ –Ω–∞ –≤—ã–≤–æ–¥–µ –∏–∑
sh_cdp_n_sw1.txt –∏ sh_cdp_n_r3.txt).

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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
    –¢—É—Ç –º—ã –ø–µ—Ä–µ–¥–∞–µ–º –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã –æ–¥–Ω–æ–π —Å—Ç—Ä–æ–∫–æ–π –ø–æ—Ç–æ–º—É —á—Ç–æ –∏–º–µ–Ω–Ω–æ –≤ —Ç–∞–∫–æ–º –≤–∏–¥–µ –±—É–¥–µ—Ç
    –ø–æ–ª—É—á–µ–Ω –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã —Å –æ–±–æ—Ä—É–¥–æ–≤–∞–Ω–∏—è. –ü—Ä–∏–Ω–∏–º–∞—è –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã,
    –≤–º–µ—Å—Ç–æ –∏–º–µ–Ω–∏ —Ñ–∞–π–ª–∞, –º—ã –¥–µ–ª–∞–µ–º —Ñ—É–Ω–∫—Ü–∏—é –±–æ–ª–µ–µ —É–Ω–∏–≤–µ—Ä—Å–∞–ª—å–Ω–æ–π: –æ–Ω–∞ –º–æ–∂–µ—Ç —Ä–∞–±–æ—Ç–∞—Ç—å
    –∏ —Å —Ñ–∞–π–ª–∞–º–∏ –∏ —Å –≤—ã–≤–æ–¥–æ–º —Å –æ–±–æ—Ä—É–¥–æ–≤–∞–Ω–∏—è.
    –ü–ª—é—Å —É—á–∏–º—Å—è —Ä–∞–±–æ—Ç–∞—Ç—å —Å —Ç–∞–∫–∏–º –≤—ã–≤–æ–¥–æ–º.
    """


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print(parse_cdp_neighbors(f.read()))
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 11.4a

> –î–ª—è –≤—ã–ø–æ–ª–Ω–µ–Ω–∏—è —ç—Ç–æ–≥–æ –∑–∞–¥–∞–Ω–∏—è, –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å —É—Å—Ç–∞–Ω–æ–≤–ª–µ–Ω graphviz:
> apt-get install graphviz

> –ò –º–æ–¥—É–ª—å python –¥–ª—è —Ä–∞–±–æ—Ç—ã —Å graphviz:
> pip install graphviz

–° –ø–æ–º–æ—â—å—é —Ñ—É–Ω–∫—Ü–∏–∏ create_network_map –∏–∑ –∑–∞–¥–∞–Ω–∏—è 11.4 —Å–æ–∑–¥–∞—Ç—å —Å–ª–æ–≤–∞—Ä—å topology
—Å –æ–ø–∏—Å–∞–Ω–∏–µ–º —Ç–æ–ø–æ–ª–æ–≥–∏–∏ –¥–ª—è —Ñ–∞–π–ª–æ–≤:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

–° –ø–æ–º–æ—â—å—é —Ñ—É–Ω–∫—Ü–∏–∏ draw_topology –∏–∑ —Ñ–∞–π–ª–∞ draw_network_graph.py –Ω–∞—Ä–∏—Å–æ–≤–∞—Ç—å —Å—Ö–µ–º—É
–¥–ª—è —Å–ª–æ–≤–∞—Ä—è topology, –ø–æ–ª—É—á–µ–Ω–Ω–æ–≥–æ —Å –ø–æ–º–æ—â—å—é create_network_map.  –ö–∞–∫ —Ä–∞–±–æ—Ç–∞—Ç—å —Å
—Ñ—É–Ω–∫—Ü–∏–µ–π draw_topology –Ω–∞–¥–æ —Ä–∞–∑–æ–±—Ä–∞—Ç—å—Å—è —Å–∞–º–æ—Å—Ç–æ—è—Ç–µ–ª—å–Ω–æ, –ø–æ—á–∏—Ç–∞–≤ –æ–ø–∏—Å–∞–Ω–∏–µ
—Ñ—É–Ω–∫—Ü–∏–∏ –≤ —Ñ–∞–π–ª–µ draw_network_graph.py.  –ü–æ–ª—É—á–µ–Ω–Ω–∞—è —Å—Ö–µ–º–∞ –±—É–¥–µ—Ç –∑–∞–ø–∏—Å–∞–Ω–∞ –≤ —Ñ–∞–π–ª
svg - –µ–≥–æ –º–æ–∂–Ω–æ –æ—Ç–∫—Ä—ã—Ç—å –±—Ä–∞—É–∑–µ—Ä–æ–º.

–° —Ç–µ–∫—É—â–∏–º —Å–ª–æ–≤–∞—Ä–µ–º topology –Ω–∞ —Å—Ö–µ–º–µ –Ω–∞—Ä–∏—Å–æ–≤–∞–Ω—ã –ª–∏—à–Ω–∏–µ —Å–æ–µ–¥–∏–Ω–µ–Ω–∏—è. –û–Ω–∏
–≤–æ–∑–Ω–∏–∫–∞—é—Ç –ø–æ—Ç–æ–º—É —á—Ç–æ –≤ –æ–¥–Ω–æ–º —Ñ–∞–π–ª–µ CDP (sh_cdp_n_r1.txt) –æ–ø–∏—Å—ã–≤–∞–µ—Ç—Å—è —Å–æ–µ–¥–∏–Ω–µ–Ω–∏–µ
    ("R1", "Eth0/0"): ("SW1", "Eth0/1")
–∞ –≤ –¥—Ä—É–≥–æ–º (sh_cdp_n_sw1.txt)
    ("SW1", "Eth0/1"): ("R1", "Eth0/0")

–í —ç—Ç–æ–º –∑–∞–¥–∞–Ω–∏–∏ –Ω–∞–¥–æ —Å–æ–∑–¥–∞—Ç—å –Ω–æ–≤—É—é —Ñ—É–Ω–∫—Ü–∏—é unique_network_map, –∫–æ—Ç–æ—Ä–∞—è –∏–∑ —ç—Ç–∏—Ö
–¥–≤—É—Ö —Å–æ–µ–¥–∏–Ω–µ–Ω–∏–π –±—É–¥–µ—Ç –æ—Å—Ç–∞–≤–ª—è—Ç—å —Ç–æ–ª—å–∫–æ –æ–¥–Ω–æ, –¥–ª—è –∫–æ—Ä—Ä–µ–∫—Ç–Ω–æ–≥–æ —Ä–∏—Å–æ–≤–∞–Ω–∏—è —Å—Ö–µ–º—ã.
–ü—Ä–∏ —ç—Ç–æ–º –≤—Å–µ —Ä–∞–≤–Ω–æ –∫–∞–∫–æ–µ –∏–∑ —Å–æ–µ–¥–∏–Ω–µ–Ω–∏–π –æ—Å—Ç–∞–≤–∏—Ç—å.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ unique_network_map –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä topology_dict, –∫–æ—Ç–æ—Ä—ã–π
–æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ª–æ–≤–∞—Ä—å.  –≠—Ç–æ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å —Å–ª–æ–≤–∞—Ä—å –ø–æ–ª—É—á–µ–Ω–Ω—ã–π –≤ —Ä–µ–∑—É–ª—å—Ç–∞—Ç–µ
–≤—ã–ø–æ–ª–Ω–µ–Ω–∏—è —Ñ—É–Ω–∫—Ü–∏–∏ create_network_map –∏–∑ –∑–∞–¥–∞–Ω–∏—è 11.4.

–ü—Ä–∏–º–µ—Ä —Å–ª–æ–≤–∞—Ä—è:
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


–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å–ª–æ–≤–∞—Ä—å, –∫–æ—Ç–æ—Ä—ã–π –æ–ø–∏—Å—ã–≤–∞–µ—Ç —Å–æ–µ–¥–∏–Ω–µ–Ω–∏—è –º–µ–∂–¥—É
—É—Å—Ç—Ä–æ–π—Å—Ç–≤–∞–º–∏. –í —Å–ª–æ–≤–∞—Ä–µ –Ω–∞–¥–æ –∏–∑–±–∞–≤–∏—Ç—å—Å—è –æ—Ç "–¥—É–±–ª–∏—Ä—É—é—â–∏—Ö" —Å–æ–µ–¥–∏–Ω–µ–Ω–∏–π
–∏ –æ—Å—Ç–∞–≤–ª—è—Ç—å —Ç–æ–ª—å–∫–æ –æ–¥–Ω–æ –∏–∑ –Ω–∏—Ö.

–°—Ç—Ä—É–∫—Ç—É—Ä–∞ –∏—Ç–æ–≥–æ–≤–æ–≥–æ —Å–ª–æ–≤–∞—Ä—è —Ç–∞–∫–∞—è –∂–µ, –∫–∞–∫ –≤ –∑–∞–¥–∞–Ω–∏–∏ 11.4:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

–ü–æ—Å–ª–µ —Å–æ–∑–¥–∞–Ω–∏—è —Ñ—É–Ω–∫—Ü–∏–∏, –ø–æ–ø—Ä–æ–±–æ–≤–∞—Ç—å –µ—â–µ —Ä–∞–∑ –Ω–∞—Ä–∏—Å–æ–≤–∞—Ç—å —Ç–æ–ø–æ–ª–æ–≥–∏—é,
—Ç–µ–ø–µ—Ä—å —É–∂–µ –¥–ª—è —Å–ª–æ–≤–∞—Ä—è, –∫–æ—Ç–æ—Ä—ã–π –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Ñ—É–Ω–∫—Ü–∏—è unique_network_map.

–†–µ–∑—É–ª—å—Ç–∞—Ç –¥–æ–ª–∂–µ–Ω –≤—ã–≥–ª—è–¥–µ—Ç—å —Ç–∞–∫ –∂–µ, –∫–∞–∫ —Å—Ö–µ–º–∞ –≤ —Ñ–∞–π–ª–µ task_11_2a_topology.svg

–ü—Ä–∏ —ç—Ç–æ–º:
* –†–∞—Å–ø–æ–ª–æ–∂–µ–Ω–∏–µ —É—Å—Ç—Ä–æ–π—Å—Ç–≤ –Ω–∞ —Å—Ö–µ–º–µ –º–æ–∂–µ—Ç –±—ã—Ç—å –¥—Ä—É–≥–∏–º
* –°–æ–µ–¥–∏–Ω–µ–Ω–∏—è –¥–æ–ª–∂–Ω—ã —Å–æ–æ—Ç–≤–µ—Ç—Å—Ç–≤–æ–≤–∞—Ç—å —Å—Ö–µ–º–µ

–ù–µ –∫–æ–ø–∏—Ä–æ–≤–∞—Ç—å –∫–æ–¥ —Ñ—É–Ω–∫—Ü–∏–π create_network_map –∏ draw_topology.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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
âPNG

   IHDR    Ÿ   ”ÛG9   sBIT|dà   	pHYs  ƒ  ƒï+   tEXtSoftware www.inkscape.orgõÓ<    IDATxúÏ›wxTe⁄{jz/§ì	=‘HÔê–ÖAA≈ÇÇà¯ÌÆÆ(`[,¨X@Ï4È"% !ÖÙûIõ>ﬂ…3)@¬§‹øÎ ^ŒyﬂÛûgÿ33Á9Á-Çû={Í@DDDDD≠û–“Q”¿‰Äààààà 09 """"¢j‚ÜnP)±CπÉWC7KMîXYá≤,KáADdBÊËçÿ “aPd´Âñ„Å)uÜZbkÈ0®ˆ•Ÿê® -Fì–‡…Aπù'nkËf©âr(ÕÑ√µ]ñÉà»ƒMø~ê€∏X:™Aÿ’ù∞/À∂tL¶O/îŸ{[:™AH‚>8ó09 ÿ≠àààZ*Å¿“›ÜÁ#5Lààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™&∂t ñ÷≥≠;ûéæ¡ûp∂±BAπ7ã p9£€.$„tr.t:¿◊ŸLÎáøRÚ∞fˇEìv÷LÈã∂nˆXÚÀ)§îïıÙ¿íë]±È‘u¸õ
 Ë’÷èÙAü O∫9@íÚd¯ÈÔ¯Ïh<4Z›yˇDDd9√;˙‚…®éÜ◊Zù˘er§ñ·ª3I∏YTfvøoÊÅµDTcªØmˇ◊sK<^jŸ˙{bÒ√kù»/ì#£∏?úMBRû¨^Ìπ;‡ÌIëH ì·µÌ5V∏‘HZurÚ»¨ö‹ZùßìsóYGk)zµı¿ÿŒX:™+∆}¥{.ß![VÅa|1 ƒÀ$9∞∑í‡˘aù!	±/._úH0*üÿ-˜∆⁄Có€æ||:˚∏"1WÜÛ7Û QÌº18‘QÌºÒËˇ6˛? YTàá#Óå¸29dr%ƒB!<¨a#cÂƒH,˝Â4ﬁ?k≤ﬂ§ÓÅ∞ëà!ì+Õ∂ªzüÈM,¢∫¯ªÿ„·û¡(,W†∏Rë†Í|¥ïäÒüòﬁxÎ∑sx}«ŸZ€p∂ïb˜≥c–—€ßìsÒò47≠69Ë’÷´'˜ERû£◊Ó1 Ü``;/¨€√∞M£’·è´ôò“#amúq5ßÿP÷?§$"!‰*áyõ$ÉC}P¶P·trÆa€ˆ)xd√Aƒe∂π€[„ƒ“<“;k]∆ü7r„≠Q≥b«_¯Ïh<Ä™ﬂ†ëù¸ÌC±fjHHGlz°…>±ËÒü≠:Tjﬁ˝˝"ﬁ˛ÌÇ·ı†Po|˚ƒP¨€ø_…¿—ÎYf˜ìàÑ¯Â©ëp±ìB≠’>®p©Åµ⁄1„∫@  ﬁ˚=÷‰1ôNªûç—k˜‡è´ôÜÌ‚3  É√ºçÍıA∂¨;.¶`P®qôùïΩ⁄z‡ÿıl®4∑>(ØÔ8kî UèÓæ˛Û †GÄ˚˝øI""jvt:`_\:>?ö °@Ä°aæñâZπ#◊≤·¡K ™∫¬’‰≥D°o∞'¢◊ÌÉZ√Ó—ÕU´M‰*Ä™«_5—ÈÄJï⁄˙`BUr0$Ã«®ﬁ†PoπñÖ?Æf¬ﬂ≈!éÜ≤˛¡^êäÖÜ}Î"U˝_RT°®ﬂ!"¢©†\ ÉFMBAY’uIMÁ„Ú1›1ª_(˛±Ò˛J…{ê°Qkµ›ä&d@´”a˘òÓê´4¯˘‹§ï◊∫œı‹§îap®Ç™‰¡ŒJåﬁÅÿ|˙:_≠zÃ6(‘€4Bˇ$·PBfçÌﬁ.¶[[h¥:ú∫ë[we""j±j_ı˚ÒW™˘ﬂÉ6∂x3¶ GVâ¯Ï"æö≈Ó‘(ÙÁ„ô”ÛqzØ¸'¶7ñ¸r
€Œß<‡»®°µ⁄‰‡ljño˚oMÏç¶ı√”˙!øLéøSÛÒWj.~9óå7Lˆ;òêÅπ¬–—ÀW≤ä–?ÿëGÆe·jN12ã+08‘O\P’©†\éãÈ¶m›i—êŒËÓÔéÕßØ„F~˝f "¢ñ√Z"ÇØ≥ÊÏÄËÆmÒÀπ‰o˘8€ççÄÀôÖàY∑üø!‘ ¨ƒ"x;Ÿbfüvò›/á2±7Ó¶Qù˛!m’„ÉÒŸ±+xÔw”¡Û‘¸¥⁄‰  VÌªÄ]óRÒhÔvÊç.æÆÓáQ·~X1∂~>w≥66ÍZt æ*9ÊÉ+YEÊç‹“™;6 «’L√ò[©Ω€zbgl
¥∫⁄èè¿{˜≈’úb<˚›â∆{”DD‘‰|:3
üŒå2ºñ´4XΩÔ"^ﬂi~¶óëVM§QXÆÄïDàNﬁ.X2≤+Óå_å@è∑~A?;D5Z91+'F^´4Z¨?áW∂û6:ØB<±}·(æñâEﬂù¥@§‘Zur  qôEX±£ÍÀW  ⁄y8aHò^€S{„RF!ﬁÿuŒPˇ–’ËtUO÷é3å7–X_ÀƒÃ>ÌÏÓà`H≈¬:ªç
˜√OOé@zQ9F|∞%ïÊß¶#"¢ñi_\:.§WMk=∑8XK∞˝B
îjÛ]ÑnüÕN≠–‚Øî<<≤· ⁄y:¢ªø;∫¯∫öù·à®>é\À¬©‰™slFd;x;Ÿ‚◊ÿTî+‘FıÓGâ°W≈ÌDB<ldTG‰ó…±ı|ÚãüÓO´Onß”Uç+∏û[Ç7p˙’â÷¡◊(9»ëU‚RF!µ˜ÅΩïΩ€zbÒô?Â˙ŸçÖz#ÿ√@Ì„¶˜
¡7sÜ 1Ø£˛ªßŒqDD‘Úlªêlò tWlº8;ûÖæÔlØw!˝ö=›˝›·Îl«‰ÄÓŸæ+7Sôn:u'_â¡OOé@‘öù&›§≠ƒ"¨ô“◊l;AÓ¯ÏQ¯;5ü…A3“jìGkiçã« @VI @,4ù–È@B:è¿¸®êä´∆Ë%Â…êVXÜ¡aﬁvwDzQπ—ö∑{aXº˜p_úNŒ≈Ñè˜f¶ "¢÷Îxb6û‹t_œå›ãF£ˇ™ıû¡ŒœŸ@’ç,¢ÜóYÑ«6˛ÅmGbÁ3U	´˛È√ÉóIÌù≤÷¸ó3ä0‚√›úq´ôiµSô~8ΩVMÓk≥Â/ç®Z>¸◊ÿTì≤ÉÒUO^’y•rƒeﬂù9|-√;¯!2–áÆöNa*
Ò£¡¥~¯Â\2ÜΩøõâ|sÍﬁ˛Ì:x9cÎ¬êäo˝\ıA∞ª£…>Ω=0∫≥R Í5	Q}Ìºòäe[œ ¿’ªû{+	Ä™±1E
≥:†÷jQT°®ıf,5=≠ˆ…ÅH(¿“Q]Ò‹–Œ8|-gíÛPR©DGåÌ‚èŒ>Æ8ôîÉˇºl≤Ô—ÎYP™µh„hÉ≠ÁìM}˝q5≥˙Ü∏ïH‹.¨ç3ûπJÅ ¯zŒ`≥1Œ¸‚ê—¬iDD‘z¨ÿÒ¬ºú0π{6<ˆˇÍ0t:`tg?º<¢+ˆ∆›ƒü7rP*W°≥è+fD∂É ,˙˛Ô‘RÉ[≥ˇ"B<Ò‘CÒ√ì√Ωnœ≥™’&Øn;ÉÛix∏g0ÜÑ˘`t∏ø°ÏZN	ñ˛rˇ=t…Ï`∞2Ö
ø∆¶¢{Äv_J3)ˇ„j¶°è®π'Jç∆P^€J»¡]ø-""jFdï*‹»óAV©2)”Ítxl„pzFäÅÌºxø0|yÚ*ˆ^NGÑØÜv¡∏. ™∆ÃùI…≈´€Œ∆æ›≠2E’˘XTn˛Nˇ¢ÔO¿€…ù}]∞hHg√™…Ê$Áó"≥∏¢±B•F$ËŸ≥gÉ¶}EŒA∏2¢!õltb°nˆV∞ïäë_&G©‹ÙKöÃs(ÕDËµ]ñÉà»D\¯4»≠ù-F£Út∞Åìçyeï(Æh^]7¬ÆÓÑ}Y∂•√x`ÆÜE£ÃﬁÀ“aPB˜¡πƒ¥+yk‘jü‹N≠’r5;π•ï»-ÂÔ5úV; ôàààààå19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19 """"" Lààààà®ì"""""¿‰Äààààà™19†˚§≥t DDf	tÕ‡˚IXiÈËÅi¬Á£8(,5Çû={6ËŸ™€†“÷’lôª´l¨¨êûù›¯“v¥∑ÉìÉ2sÛ†—hıX7˙Óá«çp8‰˙6ÍqöëJ€ KáAD @PPqS!ÇV$m‘„Ÿ⁄X£[ß0$ﬂÃ@Vn˛]Ô=j7⁄\Ô«ÏÄFàÆi≥-œÉH£¥tçf‚ƒâ»œœ«Ò„« ∂n–à≠ÎΩøH(ÑF´≠w˝˚B(bﬂ—ìÊ€âjº“	tPŸîCZa_Ô„µ46´Âñ£I◊Ua“§IÛÛ´µŒ?¸Ä‹‹\ Ä´≠ju***LÍΩ˝Øó–C°oﬂæP´’ı
P*ïb˙ÙÈË◊ØêììÉ˝˚˜cˇ˛˝uÓ˚Ó?ﬂCßNù0~¸x≥à#F†Kó.xˇ˝˜ÎÀ‰…ì·ÓÓéœ?ˇ‹§L+V¬JQ YΩö""¢j˝˚˜Gttt≠u˛¯„Ï€∑ ‡ÔÔ{{{ƒ««õ‘Î€∑/˛˘œb˘ÚÂ(¨«Ô ÖBLü>„∆çÉ∑∑7*++qÊÃ|ˆŸg»……©uﬂi£ßaÈ“•ò1c dÜÌù;w∆‹πs—©S'ÖB§§§‡€oø≈ë#GuttlKep∏m_≤âDÇç7÷ZG&ì·ôgû xzz"""ÒÒÒ»»0˝ˇoŸ≤e¯˚Ôø…ÅmE›7“˙˜Ôè'ü|:tÄH$Brr2æ˚Ó;lﬂæΩ÷õ™...¯‡ıóÒ˝˜ﬂ„‰Æ[±∏ππa—¢E4h ì…pË–!|¸Ò«(..6n§ƒ?‘ ’ôå9Ω{˜ÆµŒ¡Éëõõ©TäCá··√x˘ÂóÔ;8+++|˛˘ÁGRR≤≥≥—©S'<›∫u√Í’´k‹◊ÕÕƒ7ﬂ|c61h”¶-Záz%¡¡¡xÊôgêüüo69Ët∏ƒ :ˇ9âàË~~~>|8‰r9îJÛwíˇΩxÒbDEE!22⁄ª∏≥Zì+V ::◊Æ]√æ}˚‡ÓÓé±c«¢ˇ˛ò5kñ·Êó9———∏rÂ
Æ]ªfÿ÷£G¨_øïïï8|¯0îJ%¢¢¢ﬁ{Ô·≠∑ﬁ¬∂m€  Z± "çËæﬂ›?Å@Äé;¢¢¢©©©u÷Ô‘©ﬁyÁ¨\π[∑nΩÔ„8Ôøˇ>


∞eÀ(ïJ:ØΩˆÒı◊_◊∏Ôò1c ëH∞sÁN√6[[[|˛˘Á˜˜«æ}˚êííÇêêƒƒƒ <<è?˛8
J›K!–
`_ÿzüê±z_ÕFGG£¨¨ÃlYM€Ô◊Ãô3éœ?ˇ‹pA.ïJÒ¡`⁄¥iÿªw/bccÕÓ;n‹8ÖB¸˙ÎØF€¸q>°°°
Ö(--≠5Ü^x˝˙ıCPPÑB!ÚÛÕ?6∂™∞∫áwHDDz´WØ6∫∏y"""çc«é·•ó^2$Cá≈Í’´±`¡ºÒ∆f˜EáŒ;Ô∂	,[∂*ï
≥gœFZZ `›∫uÿ¥iû˛y8p •••–à™n\	U˛◊î$&&bÓ‹πÙòB°/ø¸2 ÀÀ1k÷,‰ÂÂ æ¸ÚKl⁄¥	ÛÁœ«Œù;QTTdvˇòòƒ∆∆"99Ÿ∞ÌëGA€∂m±fÕ¸√ÜÌâââx˙Èß1i“$|ˇ˝˜»ÀÑUÖì2®˜7Rii)d2ôŸ?≠VâD Äçç|}}R©iüO2ì'OFdd$ƒb”<e¬Ñ	®¨¨ƒó_~iÿ¶T*âBmè°£££q˛¸y√≥^ff&Nü>çMõ6°∞∞∞Œ˜ùññÜ„«èc”¶MP(j¨S·Tµ¥~]•ààËﬁtÌ⁄ŒŒŒ ÄﬁΩ{#22ëëë0Ì≥/ïJ1vÏX<ˇ¸ÛxÏ±«bRgÙË— ÄÔæ˚ŒË)ƒ°Cáêôôâa√ÜA"ëòç%&&
Ö¬–›	 ⁄∑oè‡‡`;vÃË˜G&ìa«é∞∑∑«¿Å ZI’Ò¯‰†˘	Eﬂæ} ›ªw«‰…ì1yÚdLò0¡l˝ázØæ˙*^{Ì5Lô2VV∆7;tË ???;vÃê ÄB°¿Æ]ª`mmç®®(≥mááá#$$€∑o7⁄>bƒ®’jìõ§[∑nÖV´≈»ë#°≤R°Ã•ŒôŒw˝o@-WÉıÉ	

¬ñ-[  }˙Ù¡é;esÁŒ5∫√?|¯p<ˇ¸Û0lKHH¿O<a∏ wuuÖøø?Œú9ïJet¨∏∏8TVV¢[∑nfcâàà@``†QR°w˚xÖ~˝˙¡€€ª÷˜u˚£¬òòòÎ]pó‡v”≠÷ˆààËﬁ˝˚ﬂˇ6åÉ[∑nùa˚¶Mõﬂˇ˛◊∫{˜ÓX∏p!¸˝˝€û}ˆYº¯‚ã8yÚ÷ÄÕphµZ\∫t…‰XÁŒù√¯Ò„d‘m®J<FèçÉ=ÅÓ‹π3 ‡¬Ö&Ìù?ﬁPÁ∑ﬂ~ÉH-ÇW¢$rÛ…5]¿‘©STuÈ3fÄ™©∑_åª∫∫b˝˙ıàåå4⁄Ë–°Ü±@U% ∏xÒ¢…±ÙÁRxx∏Ÿ'k111®®®¿Å€§R)BBBêêê`2¥∏∏)))Ë–°J|K “à‡òÁxWÔüZ∂z'°°°f@rr2“””Ò‹sœaÌ⁄µàçç≈ßü~j(øq„ÜQ˝˛Ûü¯Èßüp¯aXYY·±«Cdd$~¯alﬁº _˛ŸŸŸ&«S´’»œœáØØ/Å… ùòòîóó„‡¡Éı}{DDdaù:u™ıw&))	O=ı˛ıØ°wÔﬁò4ií·nˇù›[ßLôÇ≠[∑bÈ“•(..∆ÄÍ´Ø‚Ö^0J|||PVVÜ J”)Eı›H}}}MíÉ¡É√………‰bMˇ›\‘€€ I•æÒ≠kÜªÊ¿√√≥gœ6[&óÀÒ√?‡€oøEvv6ﬁ|ÛMºˇ˛˚ÿµk ò\è¥oﬂgŒú¡ÏŸ≥///¨\π}˙ÙAØ^ΩpˆÏY 0‹®4◊mHﬂÀ¡‹ÕLkkkå90˙ÏxyyA(÷ÿC¢∞∞¡¡¡∞
≥ÇSéÑZvm£[Íù|ˆŸg5ñÕö5WÆ\1ú‰ÖÖÖ8sÊLçıgÃòa‘/.))	ªwÔFœû=…ÅΩ}Uﬂ∑ö~(*++!ëH`mmmÙ•nkkã#F`ÔﬁΩêÀ9%Qs1uÍT√›ÿ;m‹∏Î◊ØGNNé·ª=##£∆…´V≠¬/ø¸bxΩ}˚vå=={ˆÑççç·w√ŒŒÆ∆~‹˙ﬂ;;;ì≤ËËh§ßß„Ôøˇ6⁄nkkk¥o}€£¶√€€ã-2[VXXà~¯J•“p…Âr»dÊß*<˛<û~˙i√ÎÃÃLlﬁºÔºÛBCC◊M666 j?oÙÁ÷ÌÜ{{{ì.E˙ˆÃ%Ω∑∑)j#ÇÀ≥u®ı™wr˛˚Ô◊x±ùïïuWΩyÛ¶—Î‹‹\îóó√””ÛV`’cjöÚTﬂ’ËŒ±
√áá≠≠≠Q∑&""j˙6oﬁltWˇvw˚;cn≤âÙÙtÙÍ’ÓÓÓÜﬂ!Å@PÛ‹Ô’wÅÖB„ª™^^^àååƒßü~jrßX_◊\“¢ﬂ¶ØSÈXâîÆ)hw¶$
v-j* +Øò-ª€Ÿ±ÃÕæ•?ó›‹nuC Lü<‘%&&………&ì≥‘∑=°V«\v)"cıN~˝ı◊:gˆπïïïF_¿˙Dƒ⁄⁄¸Ç!˙˙Œ¨8::âââàããk§Hâà®1‹∏q£÷ßŒ˜Kˇª¢øp™~CÙwYÔT”›\˝†S}Ws«0˜€uÁSçXÉ
Á
@`Rï,H©Tö]∑†!€øì˛Z∆‹yS”yËÔÔèÓ›ªcÌ⁄µ&˚ËÎ÷uÂ{¿.dJ∆öL'≥;≥[}ﬂL}˜¢;988†®®»Ë…B€∂m—µk◊>5O999∞≥≥ÉHd:cê~V§€B
Öò0a˛¸ÛO≥ÎËÎ:99ôîÈ∑⁄”'ww≥òZ ˝¯J˝9w;WWW£:z&LÄF£¡Ó›ªMˆ………ÅV´Öãã˘.C...P©T( 6ﬂ•éZ∑MÙ¯Ê¶%Ω[ÈÈÈP(7)ÛÙÙÑªª;íííå∂GGGC≠Vcœû=˜}¸ªÂs’∂≈¶˝âà®aÈªv4ƒoÕıÎ◊!ïJ—°Cì≤.]∫@≠VM™—´W/¯¯¯‘ÿuıÍ’´Ü}Ô Ü¡Õ]u◊!≥ÉÊHs≤!ŒC˝jﬂÊfaÏ⁄µ+Ä™ÓNzB°„«è«±c«Ã:V(ÜâÓ|z‡ËËà†‡ ƒß∆7»"Ç‘Ú4hr†R©PRRRÁÙ†ı°T*qÍ‘)¯˚˚£}˚ˆFeCÜ =z‘∞M$a‹∏q8r‰àÈí‡@õ§6∞)5ˇhöààé˛é}PP–}∑uË–! ¿ÿ±cç∂áÜÜ"$$ßOüFyyπa{tt4äääpÏÿ1≥Ì≈∆∆¢∞∞É2x,
1r‰Hh4√oóP]=>Aƒ¥ÊHöK,ÔV\\≤≤≤0h– √ì‡÷ZJ•Gé1lÔ◊Ø<==kÌ)q‡¿H$å?ﬁh{tt4Ñ!~9ˇK{RkWÔtwÒ‚≈&ÎË}˘ÂóÜ6WÆ\Aø~˝∞d…ú;wûûû8vÏ“””Ô:∏ç7b¿ÄxÔΩ˜…'ü ++···X∏p!rssçFÁ0 ÓÓÓuv)Í’´óa±'''H$Lû<@’#ª;√=Ù–CpwwPı!utt4‘ONN6Ã[MDD˜Áˇ¯áaQ≤;Ì›ª◊˝˛Áü‚·á∆€oøç›ªwC"ë ##√d±ß˙8zÙ(bcc1m⁄4X[[~∑y‰®’j£ô˙0d»¸¸Ûœ5˛™’j¨_ø+V¨¿ˇ˛˜?l›∫J•£FçBDD∂lŸbË"‘09hä⁄µkáMõ6ô-ì…dÜı	n‹∏Å‘‘TLò0666»ÕÕÖ∑∑7ñ.]z◊«‘jµ¯√ÒŒ;Ô‡´Øæ¬û={†T*1lÿ0ÑÜÜ‚Ûœ?GA¡≠±111»ÀÀ´q ? |ˇ˝˜?~<^~˘etÏÿ©©©		¡ò1cêêüÄù[vB.¿G¶Íù‘¥ÍP5Eú>9X≥fﬁ~˚mLü>”ßOPu'Â^íÉ∏∏8º˙Í´xı’WÒÊõo∂'$$‡ı◊_7úçúúú:u™÷6£££MÓ-_æ p¸¯qì⁄Ãô3—≥gO√k[[[C˝≠[∑íÉÿ±ãÛÉk¶+àà®˛   êëë+++√ w∫Ωˇ—£G±~˝zÃú9.ÑJ•¬'ü| (//GFFÜŸ)!KJJêëëa4VM´’‚≈_ƒÀ/øå1c∆ªº~˝:ñ/_é+WÆÍé=VVVuŒÜ∑}˚vÖBÃõ7œ0ÎçL&√ˇ˛˜?lÿ∞¡PO§¡™¬™¶fË”ÈtÜÓ=ı°V´±d…,^º}˚ˆÖ@ 0Í˙ìêê`¥J∂ûB°@||º…òïÉbÈ“•ò?>ÊÕõ†j∫ﬁ5k÷‡«4‘sqqATT6oﬁ\„L[@’97˛|º¬Üs∑≤≤[On≈‚#ã·ëÓQ„æ‘∫	zˆÏŸ(ù€¥iGGG‰‰‰‘8ˇo}âD"ÑÖÖ¡ﬁﬁŸŸŸ&6WWWÏŸ≥_}ıï—‚k“˘±ÁπB2—fggg‘ÌÁ~H•R∏ªª£¢¢¬l˜‘Mõ6A≠VcŒú9ıjO(¬ÕÕB°˘˘˘µ^»›N,C$A°PòîÕò1/æ¯"¶Lôb6˘®â˛≥ryÿÄÖ    IDATe∏d∫p>™—˝è¢©ANNé—˜C£—›Ωπ”¯Ò„!âÃN+GDD-WC%@’X∑ÃÃL≥eÌ⁄µC«éÒ÷[o’ª=≠VãºººÜ
èZµZ]„:O&L¿˘ÛÁÔ*1 ™>+•n•Pÿ*‡öŒ^T≥FK§ˆÌ€„◊_ΩßÆKDDDu	

¬Ôøˇé˝˚˜7hªyAy∞)±Å}°˘iªânÁ‡‡Äì'O‚ƒâ˜¥ø F«<GN†Bµj¥nE≠ª—›∫2Ë
úsú·ì‡cÈPàà 4°E–àààZâ\•ïÈäπDDñ¬‰†Å8‰;@"óX:""jF$r	T÷ÊßE%jH)›Sêﬂ6ﬂ“aP3¿‰†Å¥;”éyéñÉààö©B ‰Äù JÖBﬂBà‘\◊ÄÍ∆‰Äàà»B$ï(mŸ≠àWA@Djú≤ùÍÆL≠ìÉí÷9ÂÆ7•µ|÷e÷–à5PŸÈ5êê∑47√™‹Dµ·Y“@

 ∑ì[:""jFÏäÏ–˘`géY£FSÏY•çÓ©ÓñÖöâ±ŒQs$‘
aUaeÈ0®ÀÃÉcæ#¨À≠-
5Lààà,HaßÄF¨Åmâ≠•C°»9€ôâ›v+"""≤†Ïêl‹øiÈ0®ÖÚHıÄCæÉ•√†fÑ…ëŸ€°¬π:°Œ“°P¢È†∞UX:jÜòYê}°=¥"-*+,
µ EﬁEàçTcÈP®ô·òÉÒ{ß#"¢ªf]f±Bå2◊2ÿ€Y:j!r€Ê¬9«"%>£ª√´Ÿ"Râ –
,5CˆEˆ(s-≥t‘BT:U¢‹µ©ñÖö!&§‘Ω*k.bCDDwœæê…5úº∂y∞.≥Ê@d∫'LHbd"d2KáADDÕêK¶B˛
±t‘®•j¯¿#ôOËﬁpÃëÖI+•êVJ-µ ÖæÖjÑpOÁä»toò5:ëeÆep»cW∫wû…ûp uÇPÕŒ!toxÊ5eŒe∏÷˜‰ˆrKáBÕúUπï•C†få…Q`_h±BåbÔbKáBÕë HãHÉ‹Å…%›&DDDMÄ@'Äsé3
}
-
5CE^E»»∏–6›'&ƒˇí?Ï
πx›;˜TwT:VrZS∫kŸÌ≥·íÈÎ2kKáBÕìÉ‚~”÷Â¸@—Ω≥+∂É]±ÚÇÚ,
5#≈^≈®p¨Äw¢∑•C°Ä…Q‚ë‚Åœh≈ZKáBÕDv˚l8g;√FfcÈP®`r–@bGƒ≤ü(›7ót>‘ôSQRΩîxñ†‹πúO®¡pùÉ¢ëh†q›°V°Çâ’èD!Å˜Uoÿ€Z:j!ò5AπAπhHı∞t(‘ÑŸñÿ¬∂Ñâ5ﬁö ""jÇTV*dv»ÑF¨±t(‘È:»<dñÉZ &DDDMêWí  rÇs,
5A˛HåLÑ“FiÈP®Öar@DD‘âT"¥IjÉúê®≠‘ñáö≠Pã¨–,∏ßπCZ)µt8‘¬à|||˛’Pçπππ!005˛@EEEùmç;Ôæ˚.íííêôôYÔ1lÿ00 °°°(//Gqq›K—˜È”Î◊Ø«ıÎ◊ëïïeRÓ‡‡Än›∫°§§J•iñ^ÓR«|GXUX’;V""¢⁄ÿ lëòçD«<GKá”Ë·ÓÓGG«ˇ¥Z-T*Uùmç=ã/FBBäääÍÉT*Eü>}–≥gOx{{£∞∞
Ö¢Œ˝˙ÙÈÉ◊^{≠∆„Ÿ€€#$$2ôÕ˝uÀ	…ÅÃCÜê≥!iD˜’—ùt@Ú¯Ò„±h—¢ZÎ¨_ø7n º¬

¬Ûœ?oRœŒŒæææ∞±©ˇúΩ}˚ˆ≈ ï+·ËxÎTß”·´Øæ¬∫uÎj›w î)∞±±¡≈ãÕñOù:œ<ÛÊÃôÉKó.ôî∑;”Æﬁq’áP-Ñ◊5/dÑg¿#’Ve-˚‘cè=Ü9sÊ‘ZgıÍ’¯Ò« œ=˜ÏÌÌ±rÂJìz>>>àååÑÉÉCΩèﬂ´W/¨\πÆÆÆÜm
Ö´V≠¬Œù;k›˜ëGA`` íììk,_∞`¶LôÇ‘‘‘z«t'µTçÏêl¥InâBrœÌ’§Qf+⁄æ};Æ\πb∂,..Œﬂ:t@DDDÉ”≈≈´V≠Bee%,XÄ.¿€€Àñ-√ú9sp˝˙uÏﬂøø∆}£¢¢˝˜ﬂC≠æıË6   QQQ«·√$N""¢ª·ëÍIeÎπ‹πsgç–±±±ÜˇÓ€∑/\]]Õ&wÀÕÕÔæ˚.îJ%ñ,YÇÑÑx{{„ïW^¡ä+êííbtÏ€yxx†ˇ˛¯Í´Ø†’ﬁZºŒ◊◊Ë÷≠&Núxﬂ1@fX&Ñ:!⁄$∂iêˆàÓ‘(…¡ô3gjºøWB°...(..6˚8n“§I∞≥≥√Í’´qˆÏY ¿Õõ7Ò⁄kØaÔﬁΩò9sfç1ç3âƒ‰Æ@PP¶Mõ (//ØıÓCZÁ4∏e∫¡Æ–Ó^ﬂ"ë	ÅN œûñ„Å˙˝˜ﬂÒÁü>–cNõ6ˆˆˆXæ|9˛¯„ @VVñ-[Üü~˙	≥gœ∆K/Ωdvﬂq„∆A(ö\GDFFzTh4àD˜ﬂH#÷¿7ﬁ"5ªQ„∞ÿ:_~˘%BCC!ëH∞c«√ˆ~¯[∂l1ºâDò5k{Ï1∏∏∏@•R·¯Ò„¯˜øˇç≤≤2CΩæ}˚ Nù:etú‚‚b\πrù;wÜ££#d2”iøbbbkÚ(»ë#8r‰ ‡Ÿgü≈„è?^„˚)(Ä]âì""j±YaY∫Ó±íÀ˝˜øˇÖüüƒb1÷Ø_oÿ˛Ûœ?„–°CÜ◊B°SßN≈£è>ä∂m€"''¿G}d‘[†_ø~–jµ8yÚ§—qíììëûûé>}˙@$ô‹†àéé∆Ÿ≥gëëëaT∂m€6l€∂ ∞|˘rLû<˘æﬂw–˘†˚nÉ®6õ≠Ë¸˘Ûê…d–Èt8}˙¥·/==›®ﬁˇ˝ﬂˇaŒú98vÏ∂lŸÇõ7ob»ê!X∏p°QΩ¿¿@¢††¿‰Xâââ
Ö4)GHHàQÇBDD‘˘!ΩSz›[Å““R√Ö∫L&3¸›9i»õoæâ≈ã#--˚˜ÔáX,∆Ãô31oﬁ<CÅ@Ä†† §ßß›x‘KHHÄµµ5|}}M ∫uÎÜÄÄÄ:«$‹/Öù:ÅÆQèA4“ìÉ◊_Àñ-3[ˆ≈_‡€oø≈⁄µk—©S'899’⁄WÙÈ”Xµjïa‰øµµ5vÓ‹â±c«bÕö5ÜzŒŒŒfg™∫UcÓÉää
¸˛˚Ôı~DDDöH-Çˇe$ıLÇ[ÜÚÍ?–∂πY≤dâ·∑˚N_˝58Ä+V`Àñ-puu≠Òö Æ^ΩäU´V!'ßjΩwwwÏ‹π#Géƒßü~
 ∞µµÖççMç≥)Í∑ªππ!--Õ®,::•••FO+öV®≈ıæ◊·íÈﬂx”Ö®!5Jrêòòh¯ﬁ©¶¯öÏŸ≥«hJ0π\éÿÿX<ÿ–MH"ë@(B.óõmCø›⁄⁄⁄hªµµ5Féâ‘kzU"""KrŒrÜsé3R∫¶†”—N)ŸÔº.ﬂ|Ûç—5I~~>‚‚‚–•KÖBhµZXYUÕUYYi∂˝ˆ;gP¥µµ≈·√±k◊ÆzMwzØr⁄Â@%U¡3•uç=!Àhî‰‡ªÔæk…∑+-- √áY≠VC´’B"1?ìÉæﬁù‹°Cá¬ﬁﬁ€∑oo¥XâààR‡≈@\yË
R"Rr6ƒ“·4ä5k÷4ÍÄ‰ííà≈bH$(
√ÿÉöÆ#Ù€ÔÏ≤4r‰Hÿÿÿ4jó"ÖùŸÌ≥·ì‡”™f¨"Àiñ+$ﬂ>MPµñAYYYçk"ÿŸU.))1⁄É‰‰‰ß&#""jjDJœ¢ƒ´≈mÍ^‰ìL›yQ^^çFSÁuƒùìöDGG„⁄µkàèèoú@§uIÉUô<ì˘‘Äã'Å†A⁄IIIÅõõõ—hz˙Å»∑œôÏÁÁá=z4X∂Ò{\3\ÎÆHDDtü
v2Œ9Œñ≈‚Ñ¬˚øî—h4»ÃÃÑ∑∑∑ŸÈF˝¸¸†”Èå&M	

BDDD£NhRË[ôª±hÊzâ®.MJKK!ëHÓj‰öú={B°Ωzı2⁄nkkãŒù;„∆ç(,,4lèééÜF£¡Ó›ªÔ˚ÿ  Râ¯¡%"¢Êˆ©≥u¬÷9ãMyy9lll$A8wÓú·ö·vË–°‚„„ç∆'FGGC©T‚∑ﬂ~ªÔc◊Di≠Ñg™'ÏãÏÌDwjî‰†]ªvàåå4˚Á„„c®wÛÊM ¿Ãô3aee{{{£Úª±}˚v®T*,Z¥ ™æ˙Í´∞≤≤2,µT›e?~<é?nî0‹I"ë¿——éééêJ• ™í˝∂€ï∫óBe≠∫ßÿâààÓUrèd§v5øöpsÂÔÔèé;ö˝ª}Ê¡¥¥4ÿÿÿ`¯· ™~ﬂÕı ®˝zœ=˜úa—SâDÇó^z	"ë»h|¢X,∆∏q„p¯a≥Î'5Ø$/¯_Úo¥ˆâÃiî…sÁŒ≈‹πsÕñ≠_ø7nPµP…ÿ±c±`¡,X∞  ∞a√|ˆŸgw}ÃÃÃL¸Á?ˇ¡ä+∞uÎV√ﬁﬁb±{ˆÏ¡÷≠[u˚ˆÌOOOº˝ˆ€µ∂9bƒºÒ∆F€÷≠[†™øbdd§a{bd".¿Ì¶€]«NDDtØ\”]ëôô⁄$µ±t8bÈ“•5ñ≠^Ω⁄p√oÀñ-=z4VÆ\âeÀñ¡⁄⁄¸±—b™ıu˘Úelÿ∞ÛÁœ«û={êëëOOO8::‚‡¡ÉF…¡¿Å·ÍÍZgó¢Iì&VH÷œò¯Õ7ﬂ@£—@&ìa‚ƒâf˜ì;»!ëK Rq6*z={ˆl∞gëÅÅÅh◊Æ]≠uíííåV"vpp¿–°C·ÂÂÖ‚‚b¸˘ÁüHKKÉüü:tËÄã/"//œ®çNù:¡«««é3ôÅ»ﬂﬂ√ÜÉóóJKKqÍ‘)¸˝˜ﬂFuV≠ZÖààå?ﬁd•√€y{{#<<‹lôNß√¡ÉØœè=œ‰Äàà,"'8Èù“ÚWH≥áé∞∞∞ZÎ\∏p7n‹0ºˆÛÛ√Ë—£·ÈÈâ¬¬BÏﬂø7n‹@XX¬√√q‰»ìR˚ÙÈ___Ïÿ±√‰:†Gè6l<<< ì…p‚ƒ	>|:›≠À•˜ﬂÌ⁄µ√ƒâM7ﬂ.88›∫u3[¶P(Ãvm÷ä¥àªB;^¨ıﬂÇ®14hr–899·∑ﬂ~√∑ﬂ~kx
–òë%•E§°–∑a'¬`#ªˇ±|dû´´+ˆÏŸÉ/æ¯6lhˆ”;•#øm>:Ói•¥¡€'™ã≈g+z–∆çâDÇ_˝’“°5ˇÀ˛∞)±ARÔ$®•jKá”bMò0B°ªvÌj∂ÀùÀëúø+~L»bZ›ìà≈b√BjÖOààZ6üZßﬂ÷Èt»ÃÃ¨W[Ôæ˚.rrr∞fÕöªä°Mõ6áïïíììëêê`TÆñ™ëíük>hn≈∫|˘r®’j¨^Ω⁄∞M("$$ﬁﬁﬁ∞≥≥Czz:Æ]ª÷®+˝∂~~~∞∂∂FbbbÉ∂´ÍˇP<ƒ
1Bˇm–∂âÓF£HÆ≠PµÿˆÅW©† uh∂’bk(°]KÍ‘´Ã/#ﬂÈÑ"®,p>R˝tjHZ”˘(B%±´ª"=P€∂m3;æû\.«¿ÅTÕ⁄7oﬁ<ÏﬁΩ«é3©€£G£µwÍ"
±d…Lù:’(AπxÒ"ñ.]jËS/Vä·Ôk(◊	thÎﬂì&M¬G}dÿ>i“$,\∏ÆÆ∆ÎÛ»d2º˝ˆ€¯˝˜ﬂoµTRN•©w#∑@IÉ_G‰¥KÜ¬VâÄPJÔ¶[òReyÉ∆B≠õ≈íôS íÇGXÍØ4 ÈûÌêÓ⁄2fäpîe¢˝ıÜd⁄TïŸy‚ZËKáA5∞≠ÃG«+[ÎÆÿB»≠]p•”KáAw–	»ñU‡£}√+˚ÇIπZ}´+è´´+ÜéÀó/õMÓ÷ÏŸ≥Ò√„–°C¯Í´ØPYYâ·√ác˛¸˘Xπr%ûzÍ)ì}2:f@i≠ƒ¢ã†—hå∫¡Ñáá#??[∂l¡µk◊PVVÜÓ›ªcﬁºyxÎ≠∑êûûnXıW%±≈•.èﬁ˜{†:ÿû  ¥∏uWªâ4*tªe#E≠ë≈íÉßbÄ•#hP:ÆÁFMàÆıè¢&*ØTé5øùEDÏ∑Ïòâ≥fÕBVV^{Ì5®TUkÍlÿ∞æææ?~<∫vÌäã/ÌÁòÁàî~)=q¥…∫>_˝5“””çf‡âççÖB°¿À/øå±c«íz@ÓÒ:BWKW7¢{¡‰Äàà®4ÛÁœ Lû<˝˚˜Pµ>Œ≥œ>kT◊√√O?˝4zË!H$\ø~k◊Æ5∫–Ô“•p‡¿Cb†wÙËQå?0IÚ0[0^Œ^xÂÔWå ÙãêﬁIü899›√;'¢ñÄ∑„ààà,    ?˝ÙzıÍÖ”ßO„⁄µkË⁄µ+>¯‡√
Ω@’\˘ Lﬂæ-$$ƒÏ1çz9Ö9ÿRæ9!9u∆‘∂m[ @zz˙]ø"j¯‰Äàà®û⁄y:‚‘ˇÕÄMÂhì2•Râ'ûxGéAee%÷Ø_è≠[∑bÛÊÕf€íH$¯¯„èÒÛœ?“zÓπÁ0k÷,>€∂m ∏πUÕÇW^n:Ë¥¨¨Ã®ŒÌ\]]ÖÕõ7√˚≤7nv∫	±R\„¨z"ë”ßOáV´≈æ}˚ÍÒØAD-üY@RR~¸ÒG£vˇ¯„ U”eÍY[[ *+MgÏ“o”◊π›ÿ±c!â∞sÁNxﬁD–π†ZWO~Ò≈ÜÔøˇ˛ÆfR"¢ñÖOàààÍ)1WÜæoli¥…%%% ™÷‰—”è3êH$&ı•“™Ö≤îJ•IYtt4Œü?è¥¥4 ÄkÊ≠iKÀùÀaW|k∫‹'ûxè<ÚNú8Åµk◊6¿;!¢ÊäOàààöçFc≤MﬂuËˆÑAœŒŒŒ®é^ó.]å;vòÏ£¥U‚ÍÄ´∏^5(yﬁºyX∏p!Nû<â•KóM…JD≠ì""¢FR€ä ı•üY»◊◊◊§LøÌŒŸá¢££Q^^éÉöÏ#≠ê"Ë|
Ç
∞`ı,X∞ ˚˜Ô«K/Ωƒ’ëâà›äàààö~,Äπª˝wÎ¬Ö–jµË’´óIô~€ﬂˇmÿfccÉë#Gbﬂæ}êÀÂf€Ù.Ù∆'£>¡»~#Ò…°O≈øæ Tf´Q+√'DDDı$‰·___ì?CΩååËt::∂∂∂  GG«{:fQQé9Çn›∫a‘®QÜÌAAAò6m
çVa6lÏÏÏÃv)“[ø~=Fˆâç?nƒÁ>Äb¨mÇ⁄Ω˝x"j]¯‰Äàà®û¬⁄8„Í™π Êöî…Âr8 PXXà˝˚˜c‘®Q8x äää‡‚‚Ç~˝˙›”q◊¨YÉ∞∞0ºı÷[X∏p!‰r9ÇÉÉ°R©∞d…£ôå¢££ëîîÑ∏∏∏€”Øã0w⁄\Ã5Û^ ‡…'üƒπsÁÓ)^"jæò’√ÚmA(@§U¬+ÎºI˘ùy_˝uú8q]∫tÅX,6öt√ÜÜôân'ì…—Gô,xñõõã3f`“§IáT*≈Ò„«±sÁN√lD@’¬j›ªw«|PÎ{˘Ï≥œÃŒ~ :°≠ µ∂AD-ì""¢zX≥ˇ" @¢*Ø◊T¶Z≠{ˆÏ¡û={L æ˚Ó;≥˚îññ‚ÎØø6[VVVÜMõ6’zÃËËh®’j¸ˆ€oµ÷€≤eãŸÌr;9Æº
ˇ8∏Ê∏ö≠CD-«µ "ë„∆ç√ë#GPTTtOmXUX¡=Õ…›ìëë
ù@◊¿QQS«'DDD-ÄH$¬‚≈ãëììsœmt¯∆˚¬¶ƒ©›R°¥Q¬/∂sFIDMüµ J•ÒÒÒ(,,ºÔ∂\3]v"r9˚ü$Y!5Lààà»Ñmâ-:Ô âB
*ÎﬁÅàZ&DDDdñD.AÈÆÄ2ÿ“°—¬‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà 09 """"¢jLààààà ì"""""™∆‰Äààààà  bK–‘=;$vRâ·uI•π•ï8ôîÉlYÖŸ}úm•àéDè w∫€£B©∆ıæ˚+	Ÿ≈*tjÅÊÏ 7;k√ÎRÖπ29N'Á‚fQYù˚[âExaXL»¿Ÿ‘º∆ïZÅÙi_g;√Î2Ö
yeï¯+%…˘•uÓÓ„Ç)=Ç–Œ√	ˆV§ñ‚≈ˇlÃê©”üKzÂJÚÀ‰H».∆Öõf˜	Íç¡°>vwÑìçô%Âÿw;/¶B£’=®âö&uX1∂⁄8⁄òlWkµÿ|*∑É\•1*K¸œ#Ü∏¨í
H≈B<⁄€ØéÈÜπ_¡Ê”◊HÏ‘Ú,ÅéﬁŒ&€µ:~9óå'æ9ÇRπ™∆˝ÁÙ√;ì#Ò¬è'ô–}[0®#Ñxôl◊ÈÄﬂ‚“0˚À√»/ìõî€Hƒ¯dÊ@ÃÍ
 »ñUT]§	Ωô–=õ›/"⁄ö-;ëîçÈüDFqπ—ˆOfDa~T ÄLÆDQπ£;˚·…®é8u#√?‹ÖrÖ∫—c'jJò‘CVI¬ˇı ¿’Œ
ùº]˙∏xº(
+‰xÈßSFı„2ã∞Ópˆ≈•£§R	 òÿ-?ÃéOgFa˜•4U(¯˚†ñAÆ“¿gÈf Äìçºú±lt7<‹3Â
5Ê|}ÿ®æßÉ>úﬁΩ\–’œÕSKÁ≥t3‰*¨%m„Ñ≈√#0∂s æò51Î˜’Äü«ÿŒ¯Ïh<ﬁÿ˝72ã´û¬˙ªÿ["|ja¬ˇı≤J*`o%A∞áÈå)=Ç˝¸aàZ≥”®n•JçU˚.‡Û£	∏ë/ x8X„˚y√1¥ÉÍÑw˜«Z‚mY«‘ÉVßCQÖE
$Â…kl*&~RıÉ˜hÔv&ıΩ˚+~<{√ê ¿ˆ)¯ÈÔ∞≥£o∞ÁãùZnùè)•ÿw÷ÌÖR≠≈Ùﬁ¡L˜)ï´p&%“|¿‘‚W(QT°@Zaƒg`“'˚QT°¿¯à ÿ[IåÍ>÷'c;‡ø/c¡∑«âÄzuç#™KIe’˘x≥®GÆea⁄ÁêZPÜÅÌºL–Á8âe[œ »+ïcı˛ Ä∞6¶OjâZ:&˜(≥∏2πvVı¯"ìW%*ç∂±¬¢V™TÆBfI9¨ƒ"HD∆Î‹“J<µ˘û⁄|üâ∑PÑ‘ö(‘$ÁóB(¿Vj¸˘¸∞Œ(S®˙Œø,µ6Zù◊sK †ﬁøŸm] †∆±
D-ª›£ W{8ZKqÍFnΩÍ¿CÌΩ°÷jq9£®ë££÷∆ŸV
?;$Ê †T3˘$À≤ëà‚·à¸29rK+€=¨—#¿‚3`+cJè ª;¢R•∆Ÿî|HHáé„?©ÅâÖBÑy9°B©FJAÌÂΩùl1*‹´&˜¡ëkYÿpú7T®ıarp‹Ï¨Ò≈¨A ÄwøXØ}ÔÜp|{:±∆YéàÓÖ£µgÜX(ƒö˝ı;âã≠Tåı3¬…FäW∂û6*ÎÏ„
 m„Ñîï3`-°R•Üç§ÍßËtr.&}≤Y%¸é§Üa%a’‰>w±«™}L&π]  hÎf≠NáˇÏ>èˇÏ9«'˝‘*19®Oú]>@’⁄ W{T™‘xjÛ1¸r.πŒ˝Ñxa˝åÅH+,√?ûlÏp©Ö≥ãÁ£ÉµÅnPkµXÚÀ)¸ÔxÇÖ££÷Ëƒ+—–j´∫l∫9@  ﬁ‹}Œ$Yuµ≥P’ß{¡∑«pÙz jx9⁄‚çË^ò’_Œå—k˜X‚mP±g—®4ZÿJ≈hÎf©Xà^¬k€kÔ ˆÈ—+t∞A_W¨◊·>.òıÂ®Pr∂"j]ò‘É~@2Pu1&	Ò˛Å+¯¸X›è{z`˜¢—ê…ïΩvèŸi˝àÓñ˛|¥ñà Òı±kúQÉ,¶®\	çíˆj    IDAT≠NëP kâ?üªÅ˛z÷§ãêHX5Z~«≈¸v˘¶a{∂¨æ=ÜÌ⁄`d'?¯8€T&∫%ïJ(‘hu:ÿJ≈8üÅó>UÁöÔÏΩ`¯Ô'£:‚≥D·fQß◊•Vá…A=‰ó…1‚√› ™ûú\:KGv√•åB|{:±∆˝á˙`˚”#Q*Wa‘˜ >ã†—˝S®5ÜÛ—F"∆/ç«¸®∏îQàè˛∏l·Ë®5ˇÒ^T™‘êàÑÿ˚‹XLÌå◊«ı¿ªŒ’+*Øöî¡‹†P≠Ná≥©yË‰ÌÇ∂ÆLËû=˙ø™ıÑ~~j&uƒ{S˚›’ì˚MßÆc›åàÈ»‰ÄZŒVtóä+îò∞n/
 Â¯b÷ <‘ﬁ€lΩ©=Ç±˜˘1»ëUb‡ö∏í≈A»‘*UjL\ø7ã ¡¥~àÈhÈê®Si¥ò˙ŸÔ∏ñSÇçÔÖô}åßzæîQ‡÷ÿÉ;Èè‘œÏFt?¥:˚ÚŒ•Â„˘aùÒÏêª⁄_ ƒ"3sCµpLÓARûì>Ÿ ÿ∂p§…<»œÎåûÜsi˘àZ≥©úªõO∂¨—Îˆ°R•∆ñyC»u4»rä*ˇÒ^U(Ln†dÀ*pÍF.FvÚCh'£˝˛üΩ;è™<ˇˇû=ôÃdü…N Ñƒ∞ ZêEdS*$Jk≠÷ZQ¥≠óµ~h˝∏‘∫vÒk≠ª’˙Òá-7¥*
nÄÄ≤ì@V≤ìu2If&≥¸˛30d$ô,˜Î∫rIûÛúsÓ¡√ôsügã5Ñ0sd<Â-“ *zL≥›IŒ3Qﬁ–¬üñ_¿íÒ√|€î
SbÓw’‘4TJ€e%y1ÙHrpñæ<R…Õˇ¸ÇË0Ô≠æÑXC˚Øã2˘”Úh≤µÒ·˛£\A&˜\|æﬂOwﬂ^q:ﬂ≠Â⁄ó>#D£‚?´ëÊ€¶◊™YêïƒÇ¨$∆'ü-∆È+—+l1HÆn‰äøåR°‡?´˘%ø˘œvî
ü¸˙RñOIc§)úÖY…|p€b"ıZÓ˙˜V‹2ü©ËA•ıÕ‰<Ûvßãˇªq>ìÜµ'JÖÇ]˜-„øø˙!?õyååcAVè_1ùø≠úç≠Õ≈ÉÏ:Õ—Ö|dÃ¡9xÂÎ<Œãè‰ûãœÁ˝€.·¢'ﬁCßV™Â˛•SÓWeiÂÈœˆ˜e®bx˚˚"Ó˝œ∑<≤lﬁ˛Cf>∫Å∆VIëa|¸´K˝Íﬁ2w4∑Ã¿‘áˇ√éby;&z÷gπÂ‹Ú∆ó<Ìﬁ_Ωò|õ´çœÛ YÒ¬ß<≥rˇﬂœ¯Í◊∑ÿ˘Ÿ?6Û∆ˆŒ«q	q∂v„∫ó?g›Mx˜÷Kò˛»€î54ÛﬁûéNbaV≤_˝¸c~˛⁄YMIä…ì'ÂMC‘Ú”„‘›íc¿„Åí∫¿]Éî
√c⁄WRÙÆ_ÆÔÚò.èªﬂw526ïìë˜^∞√Ë3M∆Ú2ñ;å”Jâ2†V)(¨È|!ü±F(®nj≈joC£RíeË¥~YC3vgÁs˜°≠uå>Ø`á—gZCc80˙G¡„¥#ıÑ®’÷Z:]º,5∆ÄJ°§∂ŸFcÎâ±z≠öYÈÒ$DË©njıMk:h⁄öøÁü¡£œ84aÏM∞√8≠¯p=z≠öí:+Nw‡ı	R¢hTJÍ[Ï~≥ûIj¥ùF…·*;Kéùvv£˛BÈv2ÒªóÇÜD§Â‡4N˜Ôˆx(®±¯ïù˙ª=Âh˝Èì Sá6ó[ÆI—+ŒdF°ŒÓ°-'ˇ=P⁄”!â!ÏLtm≤µÒm—1æ-íT!@∆!ÑB!éì‰@!ÑBHr ÑB!Ñ8Ní!ÑB! …ÅB!Ñ‚8IÑB!ÑÄ$B!ÑBà„$9B!ÑB í!ÑB!éì‰@!ÑBHr ÑB!Ñ8Ní!ÑB! …ÅB!Ñ‚8IÑB!ÑÄ$B!ÑBà„$9B!ÑB í!ÑB!éì‰@!ÑBHr ÑB!Ñ8Ní!ÑB! …ÅB!Ñ‚8IÑB!ÑÄ$B!ÑBà„$9B!ÑB í!ÑB!éì‰@!ÑBHr ÑB!Ñ8Ní!ÑB! …ÅB!Ñ‚8IÑB!ÑÄ$B!ÑBà„$9B!ÑB í!ÑB!éì‰@!ÑBHr ÑB!Ñ8Ní!ÑB! …ÅB!Ñ‚8IÑB!ÑÄ$B!ÑBà„$9B!ÑB í!ÑB!éS; Ö«ÏzòÁ¯œ¿Õª<8ˆs5¯Æ«¡@I˚ø©°ßˇ^è@Ï ÇD9d?π¬„f®˛[ÏøÜÓ˝QÙû†%!≠u$ñ}{⁄zÒ1ëò£"»+)«ÊhÎı∏¬√ÙO0QXQMSsk˜vVx®úO"éN'¥6ΩwÏ#:á%ÿ!Ù)ùΩâƒ≤oIåç†º¶ÆOŒiDØ”QRU”Ì}[LπXvcﬁ≥º"Î_4m-¡°WÖÜÜM}}=---hú-gt<[*•ídsçÕ-445wˇ 
7† œ–|LVª¡°O©\é^Ωª´%Ê0∂®"¢è,`Ë&©'(˚ÌK1PıJr∞h—"¶Lô“eùwﬂ}óΩ{ø ..Ä™™™ın˝—≠\˝ı¨\πíºíº3:øJ•‚ä+Æ`˛¸˘òL&ÍÎÎŸ≤eoºÒG◊7ı€oøù+V√˛ê˙˙z_˘¯Ò„Yπr%iiix<8¿kØΩFAAÅﬂ˛ÈJ4 °≤ÈåbÁÓ∆o$44¥À:œ<Û.ó•Râ¡`¿n∑c∑€}€µ+	ïﬂÒˆﬂ7‡t:˘—è~t∆Áèàà‡ökÆ·¸ÛœG´’RZZ ˙ıÎŸµkWó˚)
÷ˇm=ïïï¨Zµ Ø|—¢E,Z¥≥Ÿå≈b·´Øæ‚≠∑ﬁ¢≠ÌDÇ|,‰÷ƒ*ø;„XEœ9r$≥fÕÍ≤Œ°Cáÿ∂m–û h4öööx¸ﬂÙÕò1ÉG}îázàˇ¸Á?®€ZœËˇÎ¯Ò„Y∫t))))¥∂∂Ú›wﬂÒ÷[o—⁄⁄ıãçY≥fÒß?=Ãw‹¡ñ√œÀä+xˇ˝˜;‹„Dˇ1a¬L&SóuvÓ‹È˜]÷ô|êK.πÑyÛÊa±¯øRπ€:Ω'Möƒ¨Y≥0‘’’ÒÈßür¯·”ûÔŒ;ÔdŸ≤e\r…%~Á3ôL\r…%$''”÷÷∆Ó›ªŸ¥i.◊â‡Á ¨AOBÂ˜ß=è¢˚z%98ˇ¸ÛY∂lYóuvÔﬁÕﬁΩ{xˆŸgÒx<ß›ÁL(ïJ{Ï1ÊÃôCAAá"%%Ö’´W3sÊLnπÂø¨ì©’jñ,Y¬_|·w3ù7oè<Ú---|˚Ì∑h4.æ¯b-ZƒM7›ƒ˛˝˚}u√√hâ‹o9˚õ´Æ∫ä®®®.Î¸˝Ô«Ârëôô…kØΩ∆ã/æ»ﬂ˛ˆ∑s>∑ŸlÊÂó_∆l6s‡¿ô5k_|1¯√Xø~}ß˚Nú8ëîîû{Ó9øÚ{ÔΩóÀ/øúÍÍjé9BBBw‹q]t∑ﬁzÎâ◊Ö4'ÀyÁù«m∑›÷eùuÎ÷˘íÉﬂ˛ˆ∑ù>|ùçeÀñ±fÕl6πππ§§§0{ˆlñ,Y¬ç7ﬁÿÂ9≤≥≥©≠≠Â´ØæÍ∞M°Pp›u◊±b≈
ˆÓ›€ÒHB˙=⁄VÌ9qnÆªÓ:ÊÃô”eùõn∫…˜}∂~˝zˆÌ€«⁄µk{‰¸˜‹sW^y%áÉ∆∆F¢££π·Ü¯”ü˛ƒoº—È~Z≠ñ≈ã≥i”&øÎt î)<ÒƒÑÖÖQSSÉ^ØÁÍ´Øfœû=¨^ΩöññP@Bn°ñÆ_	!Œ^Øv+∫·Üÿ≥gOoû¢É˘ÛÁ3gŒﬁyÁx‡ﬂ∫_˛Úó\{Ìµ\~˘Â¨[∑.‡æ3gŒ$::ö6¯ BBBX≥fııı\{ÌµTWWêëë¡+Øº¬Ω˜ﬁÀ5◊\„´Øo–Sõ\ãG·A1Dõ‹É·ÿ±c\u’Uùn?]ã—Ÿ˙Â/I\\k÷¨·ìO> **ä_|ë;Ó∏ÉÕõ7S[[pﬂúúöööÿ¥iìØl⁄¥i\~˘Â|Ò≈‹}˜›æDˆˆ€oÁ'?˘	W^y%ˇ¸Á?0õ0w˝÷PÙæ_|ëwﬁy'‡∂ÊÊ≥Ë≤sÃf3wﬁy'≈≈≈¸‚ø†ÆÆΩ‹ÚÂÀπ˚ÓªYµj¸„ÓÕÏŸ≥y„ç7¸ﬁ∆¶ßß≥zıj2220õÕ˜u´›N,$e_
±%±=ˇ¡ƒYπ˜ﬁ{ihh∏Ì»ë#æ?'&&RYYŸ#Á\∏p!W^y%[∂laÌ⁄µX≠VÃf3O>˘$ø˙’Øÿ±cyyÅ[˚ÁŒùKDDÑﬂøõ––PzË!úN'◊_={˜ÓE≠Vs√7p”M7qÀ-∑¯„èÉ¢*∫~$Ñ87Ay™P(»  B´’¢”È»  Ú˝DFFv®Ø”Èò7o?˘…OX¥hÍ\zÈ•@˚ˆ…M˜/æ¯"n∑€∑=êúú™´´˘Êõo|e3fÃ%ﬁƒ  //èœ?ˇúÃÃL“”Oå/à*èb‹ß„$1Ëcèã≈“ÈÄ^Ø˜5¡çFííí|?Je«
,Z¥àúú∆é€a{XXÛÊÕ#//œó ‘◊◊Û˙ÎØ¬¢Eã∆∆¸˘Û˘√˝∫7-]∫hoÈ8πÖÎπÁû√·p¯∂ã˛£±±ë≤≤≤Ä?ﬁ6≥Ÿå^Ø !!¡w›∫œ§••Ò√˛êÈ”ßﬁa˚‚≈ã—jµºÚ +æƒ ⁄[*JKKπÙ“K—h4èΩxÒb‘juáÑ∆ÂrQ]]Õó_~ŸÈKùs•á»™¿qã‡¯˛˚ÔŸæ}{¿ü≥m•äèèg‹∏qù^£W^y%èááz´’
@uu5O>˘$J•í+Æ∏¢”cgggS^^Œé;|eÛÊÕ#&&Ü◊_›◊´¿ÈtÚ¸ÛœSRRBNNnìõñiô¢∑u∂"ïJ≈kØΩÊ˚˝‰??¯‡Éº˝ˆ€æﬂßOüŒcè=FRRíØ¨ÆÆéÎØøû≤≤2_Ÿ¯Ò„©ÆÆˆ+∞Z≠‰ÊÊ˙íëSﬂ$«∆∆2sÊL^}ıU‹n∑Ø|‹∏q |˜]«˛ñªvÌb—¢Eå?ﬁ˜vFÂTÅ≥[¢è\x·Ö<¿@˚÷ÂÀó˚mÛæÂU*ï¨X±ÇU´V˘Ë ˛˚ﬂˇrÔΩ˜˙~3fçÜù;wv8ó∑Ï¸ÛœÁˇ˛Ôˇ:lø¯‚ã			ÈÄ6a¬öõõ;ºq≥ŸlÏﬂøüâ'b4ijj¬Í†9≤Yﬁ¢ O=ıôôô æñhÔÊÒ√˚~7ôL<˙Ë£Ãõ7œWfµZπ˝ˆ€˝ÿ'Núæ/Ì‹πìúú222¸∫<zÂ‰‰∞{˜näãã˝ }±¨\πíÒ„«wÿ∑!±cçµ=Ë›ânHNNˆ}üNõ6ÕÔ°|ıÍ’l›∫’˜{JJ
´V≠b˙ÙÈæ≤è?˛òˇ˘üˇ¡Èlˇr”jµLò0ÅÇÇÇ-£{ˆÏ°µµµ”qáÒÒÒLõ6çÁû{ŒÔª÷[ˇ€o˝>{<∂m€∆ïW^I¬%	|q‰2æ…8õø!ƒÍ’;¸Ë—£				∏Õ{Sπˆ⁄k€õ
i†‰UQQ·WıÍ’¨_øû>¯Ä∂∂6ñ.] ÚÂÀπ˘Êõ˘üˇ˘ ¬√√	Ô•ÁU]]MVV			Í\zÈ•(ï k………@‡¡“ﬁño/{òªﬁN¯±éo¸DÔP´’deeu∫˝–°ClﬂæùGyÑ5k÷∞q„Fﬁ}˜]ﬂvõÕÊ˚sJJ
7›tØºÚ
;vÏ 66ñU´V±h—"ﬁ}˜]_Àí˜ˇ˚©◊Í…eß^^ŸŸŸ‰ÂÂq‡AøœOQQëﬂó¶ó∑;@rr2§9™ôÇIL~≤ÃdDf≥π”kØÆÆé™™*˛ÚóøÛüˇúÛœ?ü˚Ôøﬂ7`¯‘ó7›t‡˛˚Ôß∂∂ñ)S¶pÌµ◊rœ=˜¯u_LNN∆Ìvºˆ ÀÀÅˆÎ¯‘‰`Ïÿ±§••qˇ˝˜w˚s∫UnMç§HÈˆæ¢wø{ÿ…öõõill‰Ø˝+∑ﬁz+eee~/ﬁJJJ¸Íø¯‚ãÏﬂøüßûz 7o·¬ÖÏÿ±Éˇ˚ﬂ $%%°R©(**Íp>ß”IYY#Få@≠V˚
/oÎÁ…˜_Äa√Ü<¶7∆§¥$>LË‚oB—z598˘aˇTø˚›Ôxˇ˝˜9x áè«„˜†t™;Ó∏É/ø¸“˜{nn.,`¬Ñ	æ2Ô[ﬁŒfÍhiioé4~Â
ÖÇÏÏlvÓ‹Iii©ﬂ6o›@«Ùæi>ıxµIµ‘´e‹'„:˝<¢gEGG˚µ<ùÍÇ.†∂∂÷˜∞T^^ŒˆÌ€÷≠≠≠e≈ä~›5Z[[˘Î_ˇ ‰…ì}…AW◊Ü√·¿Ètb4;lKKKcÏÿ±<ˆÿc~ÂzΩ•Ry∆◊Ø“©∏TÆˆ+?˛Òè˘Òèp€∫uÎxÙ—GŸ∂mõÔ°hÛÊÕùvıxÛÕ7yÚ…'}…·◊_MVVSßN%""Ç∆∆F†Ω[úÕfÎ0Îú∏NuG ŒŒ¶••≈Ø‹ôjåkƒ£ÚY)]ä˙õŒ∆—A{¬πk◊.^}ıUV≠ZEEEØæ˙jßıx‡ﬁˇ}ﬂÔ¸16l`Ó‹πæ‰¿{myØµSµ¥¥†R©0~c!îJ%Kó.eÎ÷≠^∏uuLÔwm	èuºß
!zVØ&˚€ﬂ:}ã®πª+'˜˜pª›=zî1c∆¯ T™ˆ§SﬂTxyﬂyÎyMò0Å‘‘T^|Ò≈˚xÎû<pÔ‘„©’˛ç·µ·TdV‡–;–∂»å}¡b±Ù”Ow∫Ω≥k"´’Íó ‰ÁÁ¯‘<›ıÊt:;\k–ﬁ≠√·p∞q„FørÔu‘’ÒNÆßrµ€≠vKrD¸qáÆ^ﬁÎÊLÂÁÁwh5:r‰SßN%..Œó®’ÍNg]Ûñüz_
		·‚ã/Êøˇ˝Ôiß:§)∂	C≠A∫ıCoΩıVßÍ›Ä¸≈_¯˝^^^N]]		'ﬁÿkµÌﬂkùMÙ‡GÂ≠Á5e ˘À_˛“aùNá”Èÿj⁄®køÓMç2É}°WÔÚﬂ~˚mØŒV‘⁄⁄Í7ê‘€¨⁄YW¶ŒZ≤≥≥ijj‚”O?xéŒéŸŸÒ¬Í√P∫îXb,ƒ∂»å}¡f≥u9mhOªﬁº_ÄÅÆ•RâNßÎpmh4/^ÃÁüﬁ·Ì±˜:ù.`ﬁµº«T:€cq´;~ôäæ≥wÔﬁ^ΩˆºˇøON4Ìv{¿	†Û˚“¸˘Û	Ûõç≠;ÜÌÜS+™˙£ó_~π√¥û‘‹‹Ï7¿›{ÔÎÏ^ÂΩ'û⁄’);;õÜÜ6oﬁ‹aõÕÜZ≠F•RuxgOm?üªNÓuBÙÖ†ŒV‘”ÍÎÎikkÎ–Õ«À€≈„‰õ®^Øg¡Ç|Ù—G~≥∆xyÎ:f†„(‹
ıöbe!¥¡Ïÿ±c@‡k√`0†P(|uºfœû›a∫\ØññöõõO{˝zèÈM\*Ys0‘u®¶¶≠V€°u N\è55˛´nÁ‰‰PPP‡õ	Êl®“j0ùzzª
ù<a√…¬¬¬hkkÛÕbÌ˜Øã.∫»7nTﬁcû∫†•KÎ¬®kø˜ù…bnBàs◊/íè«KÆª‹n7ÖÖÖå9≤√MK©Tíïï≈±c«|MÛ–>W≥^ØÔÙmöw¢@SYzÀ≠i¨1Jr–yõ¨{‚zÛv=ztámﬁk„‘n%ﬁ)¸∫ÍÜíòòp˙¿1c∆–““‚Ñ™v∂óFíÉÅ¿˚Ä®´YwÂÁÁ˚¶Ç>’yÁù‡∑xYJJ
'N<ÎVÉÍ’4GıŒö¢oö∂πª ÀÀq8~”x{ÖÑÑêíí¬—£G˝∫]r…%Ët∫N◊ÒDŒ»üâHÂP1S3”Øé¢wıã‰†¶¶ÜÿÿÿoŒ∆ÊÕõQ©T\t—E~Â”ßO«`0thŒÃ……È0kÃ…æ¸ÚK‹n7,@°8±vÅV´Â¬/ƒjµú 2º:ú∂ê6Y-πüÒNªwrˇŸ≥UPP@ii)S¶LÈ0¯sÓ‹π lŸ≤≈Wf2ô∏‡ÇxÔΩ˜ˆ´Öˆ˛æJ•“∑ø◊ò1c0õÕæÎ⁄ﬂ‚¶ÌL#¥IV
º„X:[`¨;ºì3úzùDDDp˛˘ÁSPP‡7““•Kq:ù∆πú	ó÷EiV)6c‡Ÿpƒ¿—––@ttÙ9«Èt≤c«ÜFJäˇÏUSßNE£—¯≠Ì/FˆÔﬂÔ∑(€…º”©^p¡æ≤∂ê6‘j5”¶M√b±p‡¿Åsé]qzΩ⁄Fºj’*ø∑Ù'[∑nªvÌ⁄˚ÏNö4â?˛Òè|Ú…'Ñáás‡¿ﬂˆÓX∑n?˙—èX≥f1119rÑ·√ás„ç7“‹‹Ã?˛Ò_›·√á3~¸xﬂT™Åîóó≥a√.ø¸ry‰>¯‡¥Z-W^y%âââ¸ıØÿIﬂ®'kK˙∆¿ÕÆ¢gçFø5Nı«?˛óÀEmm-’’’Ãõ7èn∏Å¢¢"ÜŒÎØø~V´(?ˇ¸Û‹ˇ˝¸˘œÊÂó_∆b±0gŒ.ªÏ2vÔﬁÌ◊B∞d…†„~'˚˜øˇÕä+∏„é;–jµ‰ÊÊíîîƒ-∑‹Ç√·‡ïW^9QŸ”æËûÆY≥fp€û={|/$ˆÏŸ√5◊\√ùwﬁ…oºÅ«„¡Ìv˚%êgÍÛœ?ß††ÄkÆπã≈¬ˆÌ€âàà‡¶õnBØ◊Û“K/˘Í*ïJñ,Y¬_|—a†˝…¢££ô4i £Fç⁄◊çiIh!#9É¢œãp!≠T˝—‚≈ãij
‹RΩeÀ_≥ÇÇ¶Mõ∆W\¡ˆÌ€âéé¶ºº¸¨∆+º˛˙ÎÃò1ÉxÄ|êÚÚr233πÎÆªp8~3(eddêïïÂ∑¶G†8KJJX±b˘˘˘|ˆÂg4^“»}”Ô√l6Û‹sœúD—Ûz%9∞ŸlX,ﬂ¢?Ål⁄¥…˜Áó^zâ§§$Êœüœ\Ä«„aÌ⁄µ@˚lã%‡M°•••√†Œ˙˙znΩıV~˜ªﬂq˚Ì∑˚ y‡Å|sÄC˚õå@≥∆úÍ±«√ÌvìùùÕ¸˘Û}Á~ˆŸg˝íçSIb–wBCCY∂lYß€¸q\.èá˚Óªè|ê[nπhÔjÙÊõoûUr˛˚Ô≈Õ7ﬂÃìO>È+ˇ˙ÎØ˘˝ÔÔÎJ¢P(X∫t)€∑o87Ωó≈baıÍ’<¯‡É‹}˜›æÚööÓæ˚Óã£A˚¸ÛJWøhí¶Mõ∆¥i”n[∑nù/9ÿ¥iÔºÛŸŸŸæEÃ÷Ø_V…ÅÀÂ‚Wø˙è<Ú∑›võØ‹·pß?˝â?¸–W6c∆ÃfÛiª•ßßÛ»#è¯ï˝‰'?·'¸ÄE/.¢Æ•Û‰Bœ…◊¿©äää|…¡≥œ>Kzz:k÷¨Òm_ΩzıY%€∑oÁœ˛3∑›voæ˘¶Øºππô˚ÓªœØÂ*;;õÕ∆G}‘ÈÒúN'w›uO=ıîo±JØ>¯ ‡lÇBàﬁ°ò<yrøY>)44îËËhÍÎÎ;ùñ≠;âéé¶°°°√˙*ïä>¯Äù;wv˘∆˘daaa§¶¶‚t:)..ÿbp2è¬Cc|#˙z=ZõLi⁄ü®T*—ÈtîóóüÛıJFFZ≠ñ£Gèvò>p“§I<˜‹s¸Ê7ø·„è?>£c¶••ã’jÂ–°Cª"û~m´ñ‘›©ÁøË>çFs⁄Æêá£√å-±±±$''c±X())¡Èt¢V´—Îıÿl∂I™NßCß”aµZ^£Fç"))â÷÷VˆÌ€ÁõﬁÎ—GeÏÿ±,Y≤§”ÓlÄ/ÜìŸıvŒ>»»ù#°0‡h<)))ùN`‡U\\Ïw3çLò0Å®®(™™™ÿΩ{7vªùƒƒD"""»ÕÕÌpù§••°P(NÕÎ]Ò822íÍÍjæ˘ÊøZ≠ñç7ÚÂó_Úªﬂ˝Ó¥üI´’2ı¬©h.‘RB¡'_ä!zOøJ˙“Ö^»O<¡≠∑ﬁ ∂m€zÂÖá=ãˆ$û∏¸∏^9á~ˇ˚ﬂ3{ˆl/^|V-ù)úXàK„"}{«ÅÅBDDD∞q„F^˝uûyÊônÔ_ûQNÕ∆}<ÖGq˙Ñ8≈¬Ö˘√˛‡[åÌLN,§9∫ô1üèA·íÎNàæ6d˚"å1ÇMõ6u:kLOPxDTEPü ”ØejµöƒƒDﬁx„çM ¥≠Z°={L1xLû<ô¸¸¸Ngà9gàìò“IƒYÀŒŒ¶§§ÑÔæ˚ÓåÍ7G5SóTG“Å$IÑí!€r–W,&áßfÃÁci
º8õg´&•Ü£„é2ÒÉâ¡E!ŒYEfMQMdlÕ8}e!DØ≤-}%º&m´ñ⁄î⁄`á"°êñ‹*7m!BàÅ&!7ÅQﬂé
vBiíÙ6ƒî∆Põ\ãG!ç4¢gÈZt ÿ√∫/Dw∏ïn^û∏≥    IDATr/»ïuZDüqjùxî«gwìÓDBï$} Êh.çã÷à÷`á"M´Üÿ‚XTŒs_uWØ∆ÑFö£õ—ÿ4¡EÖ)úXÏ0ÑHr–'tÕ:∆4}É¨{ z^ÍûTBeïd—sjRj?.…ÅËuIuXLÃÖÁæz∏‚‹Ir–G‰ÕÆb ∞áŸ±ƒZ0ôÇä⁄tmsîÿíXu]ØŸ ÑËíÙ°öa5T¶Wûæ¢›–◊»°ôáÇÜ$™áW£m’^ÏPƒP<æïKEÚÅ‰`á"Ñ8NíÉ>‰“∏®UâK„
v(bQ∫î4G7”*3âs„Vπ©MÆ≈TlíµDØ;6¸çqç§~ü*≠ÎBÙ#íÙ°ÿ‚X¥ﬂÖË)˙F=x†%\fñÁ∆≠t[KÏ—ÿ`á"Ü ó⁄EB^∆Zc∞CBúDíÉ>§r™0õ®Qç[Èv8bêPµ©–∂j%9ÁL›¶&y2jª:ÿ°à! ˛H<âyâ¡Cq
I˙òπ–åSÌîE—Dè2‘∞F[ÉÜ¿⁄tm∏UÚ“BÙæ˙ƒzÈ^+D?&…A”ÿ4òJLTdT‡VÀ±Ë∆Z#÷´o!!∫´tt)G~p$ÿaàAÆ!ÆÅÇI4ƒ5;!D'§Ì8ÚP;‘ œq¢ákåÑ’á·‘9—¥ ‹Ù¢{úZ'â§ÏM	v(b≥ÏM,"¶,Üò“ò`á#ÑËÑ$A†v®I»Kvb—5Î»¯&#ÿaà™&µÖKAtyt∞CÉî[Ì&J>∫√ˆv8Bà.H∑¢ rjú‘%’;!ƒP¶h_É%ˆh,Jß|%àﬁQ4°à6]#wåDÈíÎLà˛L˛ÖQì©â¬âÖ¥D»,3‚‹µÜ∑íwA.µÙgÆ!æ{®S±¨à,zGc\#	§ÌLC€¢v8Bà”ê‰ à¢ £0‘(>øXíäs¶µi±FYi47;1ÄK=Fde$:´.ÿ°àA*¢*Ç¨/≤0÷»zBíŸÔÜc”€®UÏPƒ ßr®0÷iHîY@ƒôK€ëF >à,z^´±’˜‚+¥14»—!Œî$A¶k—ët0â Qï4G6;1¿EVD“hnîir≈S9Uhm“’CÙ¨ñrgÂRùVÏPÑ›$…A?`.2c®1Pt~ït/g/™2
è“É≈d	v(¢ük5∂RöU*üâg◊€9ÚÉ#ËÙòÕ¡G—MíÙ√w'Æ ÖKÏPƒ ¶∂´1‘®KîY∞D◊™“´håkîôcDèrÍú˛¡a4v#ø)ﬂiB@Ú≠–Oh[µƒñƒ;1òäLËZep©Ëú=ÃN]R	GdΩ—s⁄B⁄»ùëãB° }[:*ß*ÿ!	!ŒÇ$˝åSÎ‰»é`3ÿÇä†¢ £H:êÏ0D?V1™mãñ®≤®`á"ë ÙJ 2æŒ@cóï⁄Ö®$9ËgT.Nçì¸i˘8µŒ`á#0∑ çG!cXÑ?ªﬁN]r	y	(<“ÂCÙú‰…d~ùâ∆&âÅô$˝å¬• ˝€t<x8ÚÉ#2XPúó÷≈ﬁ{±ƒ…¿d·Ø2£mãñË≤Ë`á"õ—Êk1P∏®Í G$Ñ8WíÙCjªöÙÌÈÿ√ÏN,î∑ø¢€TzãûÍTôFP¯´#˘`≤¥àsfç≤í;#óFs£Ã¥'ƒ "…A?ba‰ˆëXLä&IÇ ∫-.?ã…BKdK∞C˝HlI,ëë¡Cpµ…µ‰Õ»√–``‘ˆQ2+ëÉà$˝ò°Œ@˙∑Èh[µÚñOt[xu8açaT§ÀÍ€lˆ0{∞√É@yF9EÁa*11Ú€ë(ùÚ(!ƒ`"ˇ¢˚9cçë§É«gûë¸@tS¸·x‚hov("»J∆ïP<°8ÿaàÆ<≥ú ÙJÜÔN æêFm!Iê¬Û)SÏ0ƒ YI®%î™¥™`á"Ç®—‹HSlâáÉä‡ÃEf2∑fs4&ÿ°!zâL+0ÄDVGRx~!nïõa{á…qF“v•°µiÉFèS*ïLô2•À:Nßì]ªvù—Ò÷Ø_œæ}˚XªvÌ«†P(ò8q"YYYh4


ÿ∫u+á„¥˚˝˝Ôßººúﬂˇ˛˜ Ëız∆é€Â~€∑o?„ÿNú ≥ â¨àƒPgË˛˛b»kén∆f#Êhjªµ]ÑÃ‰_¯ UÖ“©§`J.µã·ﬂó±‚¥B¨!¡°W®’jûyÊô.Î‘◊◊≥p·B &MöƒØ˝k^~˘e6m⁄‘°nbb"ïïïg|˛––Pûx‚	¶MõÊW^XX»Ì∑ﬂNEEÁc=&Lò¿§Iìx˚Ì∑}e			ß˝<ßKÜ©M©•’ÿ àù#∫ΩØµ)µîå/!º*\ZÑ"$9`"™"HﬂñŒë©G(úT»àÔF†pKÇ NØtt)Üz√†õ©¶¨¨åW_}5‡6ª˝ƒ \£—HVVëë=Û˘˝Î_3m⁄4˛ÒèÍ´Ø‚p8Xºx1˜‹s=Ù7‹pCß˚fggcµZ&)[∑nıKŒÖKÌ¢Ïº2bãbmí(zá[ÂÊË∏£‘$◊üO“!Yu]à°BíÉ»Xc$}{:˘”Ú©YE¸·¯`á$ ß÷…—1G	?>®f©≠≠e˝˙ı=~\É¡ÄR©ƒbÈ∏ê\xx8ŸŸŸ<xêø¸Â/æÚıÎ◊3vÏX≤≥≥?~<{ˆÏÈ∞Ø^Øg¡Çl‹∏õÕ÷a{ii)ü|ÚIè|Ü∂–6tVâπ2÷@ú9õ¡F¡‰°“v¶UÏêÑ}h<!1∆Z#_e`.0;1@$L∆•rQë1Ù¶6˝—è~ƒΩ˜ﬁ¿-∑‹¬Üÿ∞aoºÒFá∫£GèÊÖ^‡≥œ>c”¶MºÛŒ;Ãö5ÀØŒ§IìP´’l€∂≠√˛ﬂ|Û ”ßOÀ¬Ö—Îılÿ∞·\?÷iÖ4Öê˘u&Í6y$Œ\·§BîN%£7èñƒ@à!HíÉLo—£tµˇ/¨^ç]/sòãŒ©Ìjírì®J´¢5bhMmZQQA^^–>&`€∂ml€∂çù;w˙’3fØºÚ
.óã◊^{çè?˛ò¯¯x|A"""|ıFåhÔø‰»ëÁÚñyÎú*''á√ás‡¿ÅÄ€µZ-ÑááwˇÉûD¶Ø›rRÔ‘ëﬂé$ÛõL¥≠Éo"!ƒÈ…Î§A¿≠tS;¨ñ åJ“∑ß£o–;$—OôäMÌ«ïêÒU∆†–>fÃòÄ}˜X∂l_˝5çÜ3f∞q„∆Nª!Ÿl6Óæ˚nøÅõoæôoºë9sÊÓªÔ¯∆-¥¥t\}∫ππÄ®®éo\áŒ¯Ò„y‚â':˝<ŸŸŸdgg‡p88p‡ œ=˜\∑f*jHh r>c>CH≥å5]≥mL* ˘@2·«¬%)bàì‰`P∫ïd|ùA¡îrg‰2b◊"´◊†S—C<ê∫;ïÉ≥RóTGLÈ¿ü}ƒjµÚÌ∑ﬂ‹Ê}P?S˘˘˘∫
mﬂæùoºëƒƒ˝ˆu:@¿1ﬁ2oùìegg„p8¯‡É:lkmmÂÉ>†¨¨åññÙz=£Gèf∆å<˝Ù”‹sœ=|ˆŸgß˝nµõ££èS#âÅ8≠öa5s}ì^≠! IïSE˙ˆtJ∆ñê?5ü§CIƒëÅ ¢£PK(ô_gö¶‚‚b÷¨Y”k«∑Z≠Äˇ√æw≠∂„÷êêø:^jµöK/ΩîÕõ7”ÿÿÿaøÚÚÚÄk,Ãô3á'ü|í’´WüQrPûQéKÌ"ÈÄÃ.#:◊⁄FÒ¯b,&q˘q$J-âBàs'…¡ ¢p+H›ìJhS(•cJÒ(=$‰%;,—Ö’áù¯EÅ,®◊∑€›°Ã;Éë78Yhh(@á`ÊÃôƒƒƒŒ;ÔtÎ¸[∂l°¨¨å‘‘TBCCimÌ|,Akx+’#™∂oª¶[ÁCá≈d°`Rö6_e`®ó≈ÒÑ'Hr0ôÕÑZC	ií&b—µ¢âEh[µ$:S]*ïÁ>CII	x–±∑¨∏∏ÿØ<''á   Ä3ùN[[€iÎxä&VFlql∑œ!Ü]≥éÿ£±$Ê&˙&µB/π+R∆cF4∂ˆ7áu…u4≈49"—Ö’ÖQë^ASÏ‡ø>öö⁄?„πŒ∞c«‹n7?¯¡:lÛÆò|Ú8àòòfŒú…ªÔæ∞%wQ6l)))vŸj‡“∏P;‘§ÓIÌŒGCD}R=uâu ËZt$Hñƒ@ê¥ç¶FÍìÍI<î(„ÑS±	ã…B—ƒ"≤6g°vº[Ç¡`=êü Èt≤k◊.†˝mø€ÌfÒ‚≈l‹∏ëÍÍjÜN~~~∑œYWW«ßü~ ¬Öπ˙Í´Y∑nn∑õŸ≥gìììCaa!;vÏ’øÙ“KQ(æŸéy¸Ò«)--Â›wﬂÂ·√(ïJFèÕö5kP©Tºˆ⁄k]∆§v®µmT∑?ã‹ú:'%cK®O®'>? Éë¢øxO¢€F|7cùëí±%X£≠å¯~*á*ÿaâ~"uw*Á§pb!£∂èp„“““xÊôgn´ØØg·¬Ö ‘‘‘Êõo≤rÂJﬂC∫’jeÓ‹πguﬁG}î#FpÁùw≤zıjúN'ÉÅöö~Ûõﬂ¯µ‰‰‰∞c« À;2sπ\,_æúÂÀó‡ÒxP(∏›n^x·Ö.«*4öâ®éËtªöjRj(]Ü“©$c[∆c∆`á$Ñ ì'O`è‚lY£≠L*@ÈQ2b◊ˇA©bHk	o!wV.qqf¸ÅR©dﬁºy]÷q8lŸ≤≈ØlÍ‘©å3•RI~~>õ7o`ﬁºy444¯Zº”ßOß∏∏ò√á˚m”jµÃù;ó±c«¢T*)((‡„è?ˆuaò0a/æ¯"ø˝Ìo˘Ë£è:çU°P0vÏX∆åÉŸl&$$Ñää
6oﬁÏ„HÕ∞J∆óêµ9ã–¶–.ˇ>ƒ–‡–;(úXHsT3¶Bâπâ®úÚBHqf$9bú:'ÖqËå˛l¥L]'|jÜ’–€ƒà]ÅWˆggÌ⁄µ\t—E\r…%ÿÌ=ªäy[h˚/‹è©ƒ$Só
ó∆E—ƒ"%†∑é)ãÖ}G∫1jªöQ[G·q¯∑⁄ç“)”Ü∫ÿíXbKdñõû§◊ÎY∞`ÔΩ˜^è' E„ã–ÿ5$‰ î≈C]CBéÊB3™6#∑èvHBàJíÉ!Jkkü•9∫ô#Sè0lÔ0¢ £ÇïËPë^AÏ—XﬂåW‚ÏÿÌvñ,Y“Â,CgÎXÍ1,&ô_g ¨3Cò]oÁË∏£4ö1ïòÇébê‰`àm%™"äÇID≈G1lﬂ∞9cçË9.ïã∫§:»¯:C˙*üóÀÂ[0≠'9Ù Fóüè°N∞ä\jUÈUT•U°k—ë˘M&ÜZπÑÁN∆†}≈Ã‚	≈∏ïÓˆVÑ
iE záfBﬂ®g‰ˆë<Ô
⁄tÚ‡—o([p?AiYûn›Òx»<¥Å{„ÈÎä†hoÂÙ√∏n'`.2£pÀ¯1!Dœê‰@¯∏4.J«îRìRCbn"	y“èy(kâl!wF.—Â—4pNµÃÑ3Tåﬁˇ°∂˙`á!N·V∫Q∫ïxî*”+1öP∑IKØ¢g©Ï Dˇ†t+â¨å$¨!CùA∫qõ}ìû≤¨2@ãß-#ÿ!â>b:v ç”Ï0ƒq--N*ƒc%≤2ÖGÅ±÷à“-cMÑ=OÓ,¢ÉàÍB¨! ‘'’ì{A.6£<(EU$H∆∫pü∂æ¢Á8Bè/Ê–ÏC∏’nbè lbBàﬁ'-¢Knïõ˙Ñz*3*AÜzÉ¨ç–¶Mõ∆≤eÀ())¡jµvkﬂËËhRRRP©T477ü—>¨\πíääänê´£⁄¯3‹J]∑ˆó¥WõÆçÚÛ )ûTåSÎdÿﬁa§ÏOA€™vhBà!@˙çà.Ö5ÑëıE’#´)œ(ß.πé‰}…DTG;¥>˜ã_¸Ç´Æ∫™À:O=ıÔæ˚. ŸŸŸËt:ﬁzÎ≠ı&Lò¿u◊]«ÁüNeeÂù?99ô˚Óªè…ì'£P¥'háÊ°ábﬂæ}]Ó˚„ˇòY≥fÒ˜øˇ=‡ˆÂÀós˜›wsŸeóQZZ⁄±ÇGf,¢ØX£≠‘'÷ì¥?	SâI!˙î$‚¥qG‚à*è¢tt)G~pÑî˝)òÃ¡≠OÈt:¬√√ŸµkuuuÎTUU˘˛ºrÂJ¬√√&›•◊ÎyÊôg0ôLº¸ÚÀ:tà§§$Æø˛zû~˙iVÆ\Iyyy¿}ÛÊÕ„ùwﬁ¡·p¯”l63q‚Dnæ˘ÊséQqvúZ'U#´à*èBﬂ®'™"äà™S Ñ
Iƒ”∂hI€ëFSl!MÌc<J•gH≠∞¸¬/∞}˚ˆ>=Á≤eÀHLL‰—Ge›∫uæÚ√áÛÙ”OÛ”ü˛îá~8‡æã-"$$Ñwﬁy«Ø¸≤À.„é;ÓË’∏ÖùsjúTè¨¶zD5
óÇ∞˙0Ùçz IÑA#…ÅË6cç—˜ÁÍ·’T•Wëêõ@lI¨åG8Ó÷[o%&&ùN«m∑›Ê+ﬂºy3{ˆÏÒ´;~¸xñ/_Njj*|Ú…'¸˜øˇı´3wÓ\<ü|Úâ_˘ˆÌ€ihh`Ó‹π¸·¿„È83qNNπππ:t»Ø¸ùwﬁaÛÊÕ ‹v€m,X∞‡ú>≥‚Ã8µN™GTSùVç¬≠ ˛p<Ê"Ûêz…"ÑËø$9Á$¶4G®É£cèRùVM“¡$"+#ÉV–Õü?É¡ÄR©Ù{Ë.((KV≠Z≈î)S®≠≠≈n∑ìôô…ºyÛpπ\|˙Èßæz£Fç¢¢¢¢Cw&∑€Õæ}˚ò5k±±±;vÃo˚»ë#3fè>˙há≠V´o0ÙôlBúª¬âÖ¥D∂w$s°YV!BÙ+íàs¢v®€«ô);Øå¸)˘Í$H&¨>,ÿ·ıäï+Wv˙ñ˝√?d◊Æ],[∂å7ﬂ|ìprrr:=ñ…d‚ˆ€ogÎ÷≠@˚@ÂÁüûÎÆªŒóÑÖÖFIII¿cxgäããÎê‰‰‰‡p8¯√ª˝9Ö=£5¢ï˙∏zÛ∂wáFZ
Ñ˝í$¢GËöu§ÌL£9™ô“¨R„mr0k÷¨N∑:tà]ªvùÒ±˛˜ˇóΩ{˜˙~ﬂΩ{7áf¯·æ≤––ˆïâ[[[√[Æ◊Î˝ 5ã/Ê≥œ>ÎˆÙ•Bàs◊€DÂ»J,&°M°òÕ®€‘ËZdZ`!Dˇ%…ÅËQaıad~ùâGŸﬁ˜›•qQt~q˘qÍAéÆg‹rÀ-Ω: π∂∂ñÃÃL4mmm∏›Ìãè)ïÅﬂ2™TÌ]úNß_˘ÏŸ≥âääb√ÜΩ´¬üG·°!æÅ™Ù*ö#õ1÷Iﬂû>$ßBLíà^·ùó€©u‚‘8…ùôKxM8	π	É&IË-mmm~ø∑¥¥ ∞æ∑≈‡‘q999îóó≥c«é^àRàÕh£`rëïëú∑ÔºA€Ç*Ñº$9ΩJ◊¨#ÛÎL¨—V 3 …ùôã°Œ@b^"∆c∆”@`≥Ÿ®≠≠≈d2‹Ó-?yù≥ŸÃå3x˛˘Á}-Bàû◊—¬±«à®ä ≤"íPK(„>á÷&´!&%˙Ñ°Œ@∆÷2æ…@·QP8±∑rp?¥:t∫ûÈ[ºwÔ^bbbHMMı+◊jµå3Ü¬¬Bööö|ÂKñ,≠÷,ÑË9•á˙§zrgÊrpŒAö#õ·§€ô$BàÅLí—ßå5F2æŒ kKñoëü™¥*ÍíÍ|„ãää
"""»ÃÃ<Ácm‹∏Äü˛Ùß('÷í∏Êök–jµæÌ 
ÖÇ•Kó≤m€6*++œ˘‹Bà™FV±wﬁ^
'¢∂´…¯&É—üè&≤J¶pB“≠HÖ∆¶Ò˝π5ºï≤‰2J≥J1õâ-éEÌËøóÊ3œ<”È∂á~òıÎ◊∞a√Êœüœ≥œ>À˛˝˚	„˝˜ﬂÁ_ˇ˙W∑œ˘ŸgüÒ≈_∞tÈR222»ÕÕ%%%Öâ'íóó«õoæÈ´;i“$RRR¯ˇÔˇuyÃyÛÊq≈W 0bƒ Óøˇ~Ïv;ãÖ5k÷t;N!è¬É]o'§π}Ãè#ƒALy¶"⁄i!B>˝˜	L√øNbn"’√´©L´§bT—•—ƒƒb<7ˆÌ€Á{ÔLQQëÔœ_˝5wﬁy'ŸŸŸòL&ÍÍÍ((( ‡‡¡É¨_øû⁄⁄⁄«ÿ∫u+µµµ~c‹n7w›u+V¨`ﬁºyLù:ã≈¬K/Ωƒ+Øº‚¥Ìëÿ≤eKó±Z≠VJKK|ˇıíE—ƒPg≥SìRCmJ-
∑Çqüé eJê#Bàﬁ•ò<yÚ‡ÍÀ!4∑“M}b=ïÈïƒÁ«s4&ÿ!(aaa|Ù—G¨_øû'ü|≤«éª{¬µ8’°=v<—øçﬁˇ°∂˙`á—Á<*q‘§÷`â±†±kà)ç!∂$]≥¨M Ñ§Â@Ù+J∑íò“b b–û∑⁄6Úß‰c.2]ç™M‰(˚Øã/æòêêﬁ{ÔΩ`á"ƒÄS5¢äÚÃr"™#Hˇ6ùÍp≈ÈwBàADí—?y@A˚ó≤“≠ƒPo†tt)•£Kâ¨à$∂$c≠LÖz™““R÷Æ]K^^^∞C¢_≥Ï‘&÷RüXOÊWô®€‘ƒ«s4ç]s˙!ƒ %…ÅË˜¥-ZRwßíº?ô∫§:já’íwA^˚
_e ˘IzsÂf!:ßŒI]Bu…u4G5£±ià.ãˆÕ€ßnìØD!Ñê;°0TN¶b¶b≠·≠4ƒ5¯ÉÊ®f⁄tmDTG¯VgB/k¥ïºy(›J"+"IÃMƒXcînCBq
IƒÄj	%‘rbÄl£©ëäå
4—G£â-ç%§©ˇÃt$ÑË;.µã∆¯FÍÍI8úÄæAOXc√øNdU$Jó,Ò#Ñùë‰@
âyâƒñ∆Rì\CÌ∞Z™“´µÑSC\~\∞√BÙ2ó∆EC\ı	ıXLP¥/∫Ëùÿ@·R]‰(Ö¢ˇì‰@⁄-âyâ$Nƒm•.°õ¡Ê€ﬁ›å¶UÉ∂U.b0iicÔºΩ†ÄöpR˜¶Yâ !3õ	!DwIr jj~≈•Y•X£¨DïEUÂ∑R≥¢ˇ≥áŸiào†!ÆÅÿíXbJc–ÿ4§}óÜ±∆(S!ƒ9í‰@ﬂd`âµPüTOyf9G«≈XgƒTl"™,*ÿ·	!Q¥O8–◊ûÿå6‘mj"™"¸&ã¨àbêB1xHr ÜÖ[ADu’∏ïn,ÊˆD¡v¢ÎQ]R∫aa ká.çè“É⁄Æ∆≠pì˜É<4vëUë€;CùAfBà^"…Åíîn%ëïëDV˙øm¨LØ§5ºç]CDUUÑ◊Ñ£t Ï&BÙ¥D¥–hjƒb∂–’L‹ë8í%°t+˚˘X4≠“P!˙Ç$BúdÙÊ—¥[iåk§!ÆÅöîî%ÒyÒ$NvxB*•á¢	EXLú:'õÜàcòÕÑ◊Ñ˚ÍIb Ñ}Gí!N⁄JhS(ÒG‚qÍú4ö˝f8:ÚÉ#h[µkåkå®ÚœHà”q´›4≈4—€Ñ°÷@de$
∑ÖGA\~«"¸÷.BÚT#D‘v51Gc|ø{Ùçz,±jÜ’‡°˝˜⁄p"+"	´b¥BÙÖk¥ï¶ÿˆÑ†9™ûˆ‰ªÒD0¸˚·¡R!Dí—
èÇƒCâ$íàK„¢)¶	K¨ÖÜ∏‡KÍìÍ—¥hkC·ñÅìbs´‹4G6£µk—Yu†Ä#”é†qh0÷1öØGmóØ!ÑËœ‰.-ƒYRµ©¸5{'¶7*À(√n∞£t)—7Ë1‘⁄Í2ª\j÷h+÷+÷h+ÕëÕxî%íp8Ö[¡∏M„$BàFÓ⁄BÙêìßV˚ŸXÏ;÷®ˆßÜÑ*GU]Õà]#Äˆπ€5v⁄Y±YÙΩeõuõß÷…ûE{(<ÑXC0‘à-é≈XgÙªû%1BàÅGÓ‹BÙùUáŒ™ÛçYpÍú∏Unﬂˆ‚Ò≈¥Ü∑¢µi	´Cﬂ†Gﬂ†'¨1LZDPyîÓˆ÷Ä®f¨QÌˇmi#uO*±≈±®jFnIXcò$ B1»»]]à>rÍC‘y_ûGKdãØK∆±«pÑ80‘»¸* k¥’7ZÂîÑAÙuá.˙è“ç∆Æ!¨>sÅCÉ}ÉﬁW-¢:"àA
!ÑË-í$JóC≠C≠¡W÷¶k√•u˘?MI    IDAT~?6‚uâu‡ÅêÊÙzB-°ËõÙÑWá:¨Á∆e"Ò¿h¢™@◊¢Î—COù:ï—£GÛˆ€o”ÿÿÿ≠}ïJ%ÉÅÊÊf\.◊Èw “””ô9s&7n§∫∫∫√v£—à›n«·pt+!ÑÃ$9¢—ÿ5hÏ'|±sI˚ìhâliˇâh·X⁄1¿∏O∆–◊à≈diü"““æF√P_—9RØe˙à8“LF‘J%•ıÕ≠∑≤´§ó˚ƒ¿Ò©√MDÑj˘<∑ß€Ìw≥1îÒ…—î‘Y…´Í¯ ;=ÕL®FÕgπÂceé !Bœñ√=˚·zõGMDE<:[= ?˚Ÿœò;wnóª<˝Ù”l€∂ÄŸ≥g”÷÷∆÷≠[;‘õ={6+WÆdÛÊÕgúòÕfÓ∏„ÊÃôÉV´•≠≠ç/ø¸í'ü|íääÆˇno∏·¶Mõ∆oºÄNß„™´Æbﬁºy§••°◊∑∑ÑîññÚüˇ¸á˛Ûü8ùŒ3äK!+IÑËÁ¥6-⁄J≠oV$¿oÏÇKÌ¢9≤ôöî‹j7x⁄ﬂ¯ÜXCH›ùä∆Æ¡≠r„Vª}ˇpÖÓ]<ëﬂ˛p"°öéüıXìç'?Ÿ√#~¿/ÊdÒ≥ôÁ1Û—|ù_ÂW˜Á≥œ„¡ú©|∏ˇ(ãˇ≤—oõF•‰ì_-a_y”yª√yTJ/]w!ôqëòÔ¸G~¬æOVVÖÖÖÿl∂”÷ˇÕo~É≈b·Í´Ø>ÁsÎızû}ˆYíììy˚Ì∑),,$55ïÀ/øúÃÃLVÆ\â’j∏oxx8sÁŒÂ_ˇ˙mmm ƒƒƒp˚Ì∑S[[ÀW_}Eaa!F£ë˘ÛÁs€m∑1r‰H÷Æ]{Œq!ƒ@6∏üÑ§îÆ-—e—DóE`≥”ﬁJ´±õ¡Êß`ç∂rx˙aT!Õ!ÑXèˇ4á`®3ö§·˜K¶∞v…$æ;Z√ˇæ∑ãÔè÷‚r{H3YêïƒıdrQf¢/9¯Ù`9?õys3;$f$ 0+=µRÈ◊≤0u∏â0ùöMá¸[d%1sd<?ó¬¥·fé5ù˛az†Xªv-Ï”s._æúa√ÜÒ¯„èÛÊõo˙ ÛÚÚ∏˜ﬁ{π˙Í´y·ÖÓªxÒb¥Z-6lïµ∂∂Ú√Ûﬁ{Ô˘u%zÈ•óxÎ≠∑∏‰íKxÏ±«hjjÍΩ%Ñ˝‹‡x"B †k÷°k÷YÈW÷∆®oFa7ÿ±lÿ6öböpÑ:πs$ëëxÚ.»C€™E◊¢C€¨E◊™kÔwÆpwr∆˛C£RÚÎ„hhqp—Ô—ÿz‚·ÔhΩïÕy<¯˛w,õ‚+ˇÙP\îô»√øÛ;÷iÒl-®fzöô…©±l+<—g›õ8|z®Ã/ÜÏ	©\:n gˇˇ;ÎIçÜï+W¢◊ÎQ©T\w›uæm_|Ò~ı”““∏Ï≤ÀHLL§ººúè>˙à˝˚˜˚’ô7on∑õ˜ﬁ{œØ|„∆ç‹u◊],X∞†”‰ ''á}˚ˆëüüÔ+´ØØˇˇ€ª˜®™´¸ˇ„OWIPIêHÒírõDQTr*˝ô96SZYiÕ¨Ôrf*Kß‘ô“\V“wLgp&3-ºÂ-Q”îØ„Öº§xDDADA‰r¯˝Á‰âs≤∆î◊c-÷ÚÏΩ?˚ÏsH˚º?{ø˜&99π^€¢¢"≤≤≤≈ﬁ^âˇ"“¥)8iÏ+Ìq/páÀr£}Ì2$ÄCÆ≈ÆT‹QA±o1Wö]©]¶.-Åí'ˇÀ£nw'‹\Ÿósﬁ"0∏⁄ï™jñÔÕ2øŒøxôßâæ€'É˘Üﬁ430uıVø¯ ±¡~¡Al∞Âï’ıf∆/Ne¸‚T æÛº›ö˝ÃüÚ◊À——ëq„∆–ºysÛüŒù;g<ı‘S0Äööjjjprrb¯·å=⁄ ÿ€€”°CNú8QoÈ–ÂÀó9zÙ(ù;w∆……©^BqßNùf⁄¥i{€∂mÈÿ±#{ˆÏ°∏∏¯'}~ë€ÖÇëõ ::öp-Zƒ˘ÛÁumÎ÷≠ÒÚÚ¢®®à≥gœ6Ëö.]∫–øñ,YB^ﬁ7¥Üj¥n›ö¢¢"ÏŸSSÛC¬n•s%Æª;∂QcºŒóñSp©úÆ~ƒuæìîÙ”◊øH9úC∑∂›¯Õ]ﬁ|{¨ˆ˚åˆ£§ºÇáNs‡t!}Ç€◊ıµKëÌDﬂÌ√ˇe‰qπ≤È$Ø˛Ówø≥˘ﬂÍ∫uÎ8vÏ¨Y≥Ê∫9º˘Êõl⁄¥	£—»¿Åy„ç7=z4'NjÛmﬁ¨a0ÒÒ·‘©Su			îóó≥~˝zõch◊ÆQQQ¯˚˚Ozz:Øø˛˙ıæë€ûÇëzÈ•ó<x5€Lü>ù6 0tËPjjjX∂lYΩv···å5äuÎ÷588

‚ç7ﬁ $$ƒ\vÙËQﬁ~˚m:tÕkü|ÚIBBBò;w. å7éÿÿX‹‹‹ÃÌJJJX∏p!III‘‘‘òwO≤´ÙΩ%˛µòÚ’>—ì‚ŸïuéˇÀ»„ªSÏŒ* ˝lë≈NE&”sô◊çæ˝Ã¡Aü‡6l;~ñ*£ëoéÊÚdtGsﬁADª÷4wv¨óopª8p†Õ∫#GépÏÿ±˜5n‹8ãÂ>+V¨`Ãò1tË–¡\f⁄IËÚÂÀV˚(++≥hg‚‰‰ƒ<@JJ
•••6«pÔΩ˜2i“$ 222¯Ï≥œ8wÓ\É?Éà»ÌÍ¯ﬂΩ»ØÉ≥≥3ÓÓÓÏ⁄µÀÊ6åWﬂËè5ä™™*´¡AcπªªÛ—G·ÊÊ∆‹πs9q‚å=ö?¸ê#FX›«jÅòò>˝ÙSÛ˛m⁄¥a–†AÏ€∑è={ˆêììÉ∑∑7√Ü„≈_ƒ`0∞`¡Ç˜€áõíWrô?>Jd`k"[õÎŒñî1Ô€√ºΩ&Õ"`Î±3TTâˆc*i8⁄Ëy∑/SWÔ`Ûë\∆˜ÎJXÄ;≥ÚmÊ‹Ó∆åc3 ∞uoãµs
ÚÚÚ,ÇÉÎ±≥≥∞òÈË€∑/ÓÓÓ¨\πÚö◊ß§§∞wÔ^<==Õâ»+WÆdÍ‘©Éà»ÌH¡ÅH#%&&≤ˇ˛ˇÍ{é1Ç÷≠[3e V≠Ze.œŒŒfÊÃô<˛¯„Ãú9”ÍµÒÒÒÿ€€[Ï⁄rÓ‹9û~˙iˆÓ›k—v›∫u,]∫îﬂˇ˛˜¸„ˇ®w„u+X∫'É•{2h€Í∫˚{ÍÔ…oÓÚ&ÆÛùº∆=~≠x¯„ÊˆóÆTÚüÃ|z˘‡‚hOw/Ópv`À—⁄=Ù∑;É±¶ÜÿémÿôïOl∞À+Ÿï’¥û2óïïQRRÚãıo⁄nÙÍ˜pqq±⁄ﬁ4c`jg2x`≤≥≥˘ÓªÔ¨]f—vv∂π≠óó			¨\π≤ﬁﬂë¶D¡Å»œÃ`0¬/‡ÓÓNMMçEbÊ∆çÎ-äàà`¯·¥m€ñ3gŒ∞vÌZRRR,⁄ƒ∆∆b4Ÿ¥iìE˘∂m€(++#66÷fp0h– ˆÓ›Kvv∂π,??ﬂÍLCNNßNù"((ggÁÌkˇkïSTJNQ)´ˆü –”çˇ¸iCªﬂE†ßYÁÿÆ2Âp1|πÔ.z‹ÌÕ≈ÚJˆú¨Õﬁ.,Ω¬æúÛÙ	n√˚)ËŸﬁ«Í°iÚ”S˝QPP@EEVÎ=<<0çˇ˚˘˘¡‹πsÿ<xê>}˙§‡@Dö¥¶}å™»/¿`0G≥fÕpuu%..Œ¸„ÁÁg—ˆïW^!11ëŒù;”¨Y3bbbò1c111Ê6ˆˆˆ‹u◊]ddd‘[C]]]Mzz:m⁄¥±»0È÷≠AAA◊]bqıÿΩºº())π•k≤Œ_4/Ú˜∏√¢nczm˛@ﬂé~ÙÈ‡«ˆg-n˛7…•W{_¢ΩkÛé4≠%EçQYYâ££„ı^á—h‰»ë#·ÓÓnQÁÍÍJpp0«è∑ÿ©h‡¿Å‘‘‘‘€˙¥!|}}t∆Åà4yö9i§Q£FŸL"^µj`‡¡¨X±Ç™™*~¯aõ}πªªÛÏ≥œöó@DFFíòò»„è?Œ∑ﬂ~@´V≠ptt¥π§√îˇ‡„„SÔ∆&!!Å“““z3∂4tΩˆØQ∞Ozµ˜e¡ˆ#VÎ∫›ÈIµ±Ü£yñ9#;≥ÚπX^…˝]Ó$‰NﬁYcπ$Âõ#gò◊çâ˜◊&É7µd‰∆»ÀÀ£[∑nxxxPXXxC}mÿ∞ÅêêÜfëÛ√cooo±ë¡``–†AlﬂæùÇÇk›Ò€ﬂ˛ñ™™*6oﬁåÒ™‡/$$Ñ¯¯x   ÿπsÁçYD‰Vß‡@§ë˙ÙÈc≥nÔﬁΩ8p†¡}Ω˘ÊõIûªvÌ";;õ¿¿@sY≥fµ{Â€zíoJ5µª˙∫∞~˝˙%å˙˙˙2i“$.]∫ƒ¸˘Û¸~-Óprd˛»>åÎ€ïˇ›öN ·≤/·Ï`O∑;=˘ÛC°‹„◊äè∑"ØƒÚ˚®¨6≤ÂËv´=¿Ãîo`≤ıÿ™ç5¸ø–ª8w±ú˝ß≠áw8;‡TwàñΩ¡;;hÂÍl~èKW*≠^w+ò9sfΩº ìwﬂ}óm€∂ı◊_∆ÇHKK£yÛÊ¨^Ωö-[∂4˙=ììì4hœ=˜;v$33ì¿¿@˙ıÎGFFKó.5∑çåå§Mõ66ó◊AÌé_£Gè&??üΩ{˜RRRB@@ @Ìnc∂6i*à4“SO=ıã&$X,?2ÌÏbk∑ÈD◊Ô á´´kÉf<<<¯‡ÉpwwÁ˛Á8}˙÷[6s∂§åısËﬂŸèƒ?Ù™W_e42g”˜º˙≈´◊ßŒa`∑ .]©d˜IÀd„ó+¯ÓTÌZ≥˘H.∂ñ≥œŸáﬂE‹mQV¯~ÌI¡+ˆe1dÓ◊?·ì›\ôôô◊}ö~uôúúå´´+< Ωzı¢††¿<£uÚ‰IvÓ‹i5XMOOØó\\^^Œÿ±cy˛˘ÁÈ”ß˝˚˜Á¸˘Û,_æúƒƒDãˆÉ¶∞∞–§XcöÕãää¢{˜ÓxyyqÒ‚E∂oﬂNRRírDDPp Ú´SUey∞ñÈË«3&¶][~|älBB◊ù…ÙÙ‰£è>¬ﬂﬂü…ì'õó3›jŒ\(„Å9kjÓB\Á;È‰€W'™ç5ú8W¬∫Éß»)≤ΩÔ˝g;Oê[\FqYï’ıìçü_¥ç@O7ÊŸÏcˆ∆|ôñiµ.∑∏Ãj˘Ø›¢EãX¥hQÉ€çF.\»¬ÖÎ’}˘Âó|˘ÂóVØ{ˇ˝˜≠ñ_∏pÅÈ”ß3}˙tõÔÈÊÊFü>}¯¸ÛœÎ˝˝πZnn.ÛÊÕcﬁºy◊˘""MóÇë_–œ±kKqq1•••x{{[≠˜ˆˆ∆h4Zúñ@hh(≥gœæfﬂ˛˛˛|¡xyyÒÍ´Ø^Û©Î≠¢‡R9ãwù∏~√…øxô•{2l÷Ô :w›ÌKwd‰≥ÎÁM»/Á¡ƒŸŸŸbõ_˘i¥[ë»/‰ ï+899˝,}8p ???|||, õ7oNpp0Gé±ÿµ%!!Å™™*÷¨Yc≥œêêÊœüèõõ/º¬mH”T^^Œú9s»Ã¥>k#""ß‡@‰rˆÏY|||

∫·æL7˘£Gè∂(5jÉ¡"∞∑∑'>>ûoø˝ñ¢"ÎK`¢££˘¯„èπxÒ"O<Ò˚ˆÌª·1ä‹,+WÆ¥∫åIDDOÀäDÈÍ-lÚ‰…ÊııÎ◊Õ'ü|¬·√áqssc…í%?iÈ√∫uÎàèègË–°tÈ“ÖååË⁄µ+˚˜Ô∑X«MÎ÷≠Yæ|πÕ˛"##qvv∆€€õ§§$´mRRRò6mZ£«*"""∑."¥oﬂ>Æ˝WÊ‘©SÊ?Ø^ΩöÀó/Û–C·ÌÌM^^ûyŸ√¡ÉINN∂∫m‚∂m€,N3Ü⁄$œ	&Ë£èÀΩ˜ﬁKQQsÁŒÂ”O?≠∑§(??ü;¨Ô ˝˜ﬂìúú|Õœr‡¡k÷ãàà»Ì«.<<ºqgÃã»Øñáák÷¨!))âƒƒƒü≠ﬂ}˜>NïÉı›í‰ˆ”Â‡Röï€ﬁïIDDn_ 9πç<Ù–Cÿ€€k◊˘Ià‹F222xÌµ◊»……πŸCë[êrDn#©©©7{"""r”ÃÅààààà 
DDDDD§éÇàààààH"""""(8ë:
DDDDDPp """""uààààà†‡@DDDDDÍ(8@¡Åààààà‘Qp """""ÄÇ©£‡@DDDDD """""RG¡Åààààà 
DDDDD§éÇàààààH"""""(8ë:
DDDDDPp """""uààààà†‡@DDDDDÍ(8@¡Åààààà‘Qp """""ÄÇ©£‡@DDDDD """""RG¡Åààààà 
DDDDD§é√ÕÄà¸˙µºêM•C≥õ=˘o®{c≈ÕÖàà‹$
D‰∫⁄emπŸCëˇ-+@¡Åààààà‘Qp """""ÄÇ©£Ñdπ≠ŸŸŸ·ÁÁgQñõõKMMç’ˆﬁﬁﬁ8::Zî]æ|ô¬¬¬_låøv]∫t·O˙ì˘ı≤eÀHNN˛…˝⁄¥icQVRR¬≈ãtΩááÕö˝∞{VYYEEE?y<""Ú"r[sttd≈äe≥fÕb—¢EV€ø˜ﬁ{tÈ“≈¢l√Ü7«çÂ‰‰ÑããÂÂÂTT‹z€Ñû={ñ§§$ÓªÔ>Ü¬∑ﬂ~{C˝µj’™ﬁÔ$--çgü}ˆ∫◊∫∏∏∞xÒb<<<Ãe+V¨‡/˘ÀçIDDjiYëà‹÷***ààà ""¬¸dz¸¯Ò‹{ÔΩV€è9íààRSSYºx17 <˙Ë£l⁄¥â#F‹P?7Kaa!)))9r‰gÈÔ¸˘ÛÊﬂâi',,å∞∞∞Î^;tËPs`∞p·B"""àà¸åàHìRZZäÉÉ”¶M£eÀñ7{8ú9sÄßü~˙öÌúúú9r§πΩàà¸¸àHìíòòH~~>>>>Lù:ÉAˇﬁlˇ˙◊ø®ÆÆ&**äÓ›ª€l7tËPJJJnxYìààÿ¶úiR
y˝ı◊ILL$::ö'ûxÇ4™É¡@BB$  Äöö233Yµjk÷¨1/ïi›∫5ØºÚ
ÅÅÅ <¯‡É˘S¶L·πÁû√€€€¢ˇŸ≥gsˆÏY "##y¯·áô5k˘˘˘ ¥m€ñ_|—‹>77ó9sÊò_˚˚˚3r‰H¬√√iŸ≤%≈≈≈ÏﬁΩõ§§$Nü>mn◊•KFéi~Ωj’*≤≤≤x˛˘ÁÈﬁΩ;éééú9sÜÒ„«S\\lıªàéé&!!¡¢l«é,_æº¡ﬂgNNÎ÷≠#>>û—£G[|6”¨¡ÏŸ≥m.	pwwßˇ˛ƒƒƒ–Æ];Zµj≈ÖHKK#))âÏÏlãˆ”¶M3àŸŸŸ$%%1fÃz˜ÓçõõßNùb…í%¨Y≥¶¡üGD‰V¶Gf"“‰§••1wÓ\ ∆éKDDDÉØµ∑∑Áo˚ØΩˆ˚˜ÔgÃò1å7é£Gè2e ﬁzÎ-s€+WÆêûûnæ©?wÓÈÈÈÊüÍÍjNú8Åªª;qqq∏∫∫íûûŒï+WÃ}:î∏∏8‚‚‚ÃeÂÂÂ§ßßDÛÊÕ…ÃÃ4◊EEE±h—"∫vÌ ¥i”>|83fÃ 44îœ>˚åps€Kó.ëûûŒw‹A\\···Ãõ7è™™*ñ/_Naa!]∫t¡≈≈≈Ê˜QXX»ô3gË◊ØÉÅÙÙts`”ÛÁœ«h4rﬂ}˜RØ~‡¡îññííírÕ~˙˜ÔœkØΩFII	¸„yÙ—Gyˇ˝˜È÷≠ˇ˛˜ø	∂h¯arssâãã£Gè|¡çFﬁˇ}ﬁ}˜]\\\ò:u*œ?ˇ|£?ìà»≠H¡Åà4I.dÎ÷≠ﬁyÁ<==t›®Q£àççe’™UÃô3áÃÃLé= ¨Y≥ÿæ};ÒÒÒ<¿@ÌˆúIIIÏŸ≥¿¸ÙﬁÙSQQ¡ä+Ã3ÉÅ§§$Û∂ú...ÙÍ’®ΩÈ5)((‡”O?≈ÀÀãyÛÊ±j’*†v†3f‡ËË»Ñ	ÿΩ{7Ï‹πì	&‡‚‚¬å3pww~xR˛›wﬂ0|¯p^˝uﬁ|ÛM˛˛˜øÛ +Ø\˜˚(**"&&Üœ?ˇúIì&ëîîƒé;Ù]^-;;õØø˛Ägûy∆¢Œ——ëQ£F±`¡åF„u˚2j«é#//è≠[∑ÚÚÀ/„‚‚¬K/Ωd—v·¬Ö,[∂ÄŒù;≥eÀfœûÕñ-[X∑nc∆å·‚≈ã<˘‰ìtÎ÷≠—üKD‰V£‡@Dö§ööﬁzÎ-rssÒÙÙ¥X^bãÉÉè=ˆ ã/ÆWo∫…|‰ëG5ñ¥¥4
âàà†EãÊÚËËhÚÚÚ(,,$$$Ñ÷≠[õÎ"##)//Á¿ÅÊ≤!CÜ‡ÓÓŒˆÌ€…ÀÀ≥xè‹‹\RSSi’™É∂:é={ˆêññf~ùììCø~˝Ã3?»¸˘ÛYªv-3gŒ¥yvDCôf¢££-ñ_4àää
÷Ø_›>÷Ø_œ/ºPo,999ú9sÜzÁXòTTT≈_Xî]∏pÅıÎ◊cgg«∞a√~¬ßπµ(8ë&À¥Ù§¢¢Çp∆é{Õˆ¡¡¡∏ªªSQQAFFFΩ˙ì'Opœ=˜‡‰‰‘‡qçFæ˘ÊË”ßèπ<..é6∞yÛf}˚ˆµ®€¥iì≈ìÙ»»H†ˆ…π5¶rSª≥∂UiIIâ’ßı]∫t·ìO>a˜Ó›Ãü?øüÚ˙233ÕÀÜL;988òÛB2kPVVFII	ëëë:î±c«2n‹8∆çá´´+∏ππYΩˆ‹πsîññ÷+?tË¿5sDDn
D§I;tË≥gœ‡â'û†gœû6€öû‹;99±c«vÔﬁmÒ≥tÈR†ˆÜ∂°ÀîLL7≈¶‹gggzıÍ≈∆çŸ∏q£EùÉÉ±±±Êr/// õß9 ‘KÄ6±ït¸c°°°Ãô3«ú´‘†Î¬4{CßNùàèè«h4≤vÌ⁄]ﬂæ}{æ¯‚IHH¿◊◊777‹‹‹∞∑∑∞9CdÎîe”˜÷ÿﬂ©à»≠HªâHì∑d…BCC0` SßNÂ¯É’v’’’@Ì”ÈÅ^≥œKó.5j{ˆÏ°∏∏ò»»H‹››	#??ü„«ècooOQQ°°°xzz“°C***ÿ∑oüEUUU 6óÕò MÌ~™Æ]ªÚÍ´Ø“°C^~˘eﬁyÁFçı≥ú˛|‚ƒ	æ˘Ê˙ıÎ«ò1c

b˛¸˘ÊÔ˛ZÔΩ˜m€∂e∆åıñÖÑÑòÛ-l]oçÈ{k»DDnuö9ﬁ~˚mNû<Iã-ò>}:ıüù‰‰‰ ‡ÍÍJUU%%%6≤Êj’’’|ÛÕ78::“ªwo˙˜Ôoû0’ôñ≈≈≈±yÛÊzÔaü≠'‹¶ÚSßN5jl?∂xÒbvÓ‹…¢EãHMM•CáLò0·Ü˙º⁄'ü|BMM111ÿŸŸ5x—ˆÌ€”∂m[***HNNnÙ˚öf^lïÁÊÊ6∫Oë[çÇjg&MöDyy9!!!V∑7=yÚ§yü¸Nù:YÌg÷¨YÊmRMLOúÌÏÏÃeAAA¯˘˘Y¥3=ÙΩ{˜∂X6d˙ÛÄàççµ∫•ßÈp0[[≥örnÙ1”ÃÉ)©ª††ÄGyÑﬁΩ{ﬂPø&GèeÎ÷≠ ¸ÛüˇlLá)X™™™≤ömÎÊˇÍ˙6m⁄‘+Ô—£ ˇ˘œ4ë[ôÇë:«èÁØ˝+`}âIMM~¯!Pª›¶iª…}˜›GLL_}ıïEπiÕ∫iIãùùùyM¸’vÌ⁄EII	QQQú?ﬁ"±x˜Ó›\∏pÅ∞∞0™´´ŸªwoΩÒ≠[∑éc«éqœ=˜fQIÁŒù9zÙ®yÀ–üCaa!ì'O¶¶¶Ü…ì'€Ãgh¨…ì'3x`V¨X—‡k≤≤≤(--≈’’ïÿÿXã∫∏∏8ZµjuÕÎ+++Îm£⁄©S'zıÍ≈ÂÀó˘¸Ûœ<ë[ïΩüüﬂ[7{""ø¶MõF\\:t¿◊◊ó=zP^^^Ô¥\®}jÌÎÎK«é˘˛˚ÔIMMµ®œÃÃ‰“•K2Ñû={‚ËËH`` CÜa¸¯Ò,[∂å§§$ãkŒü?œ∞a√˜˜Á¬Ö2Ñ––Pﬁ}˜]ã$X£—HªvÌËÿ±#_~˘%ªvÌ≤®§c«é¨^Ωöm€∂’ª—h$55ïﬂ¸Ê76ggg<<<0` Øæ˙*YYYLú8ëíí†ˆ$Â?ˇ˘œDDD‡··Åßß'ëëëx{{[lëÍÂÂ≈‰…ìâää¬ÀÀãV≠ZŒÒ„«Ò‡±«√ÀÀãñ-,’°ä  ìIDAT[“£G¬√√9|¯∞˘}¨yÁùw0` wﬂ}7æææÙÏŸì¨¨,s2uee%/^¥ò0ù†‹Ω{wZ¥hAÀñ-	√¡¡Å„«èc4…œœßwÔﬁÙÎ◊¸˝˝2d}˚ˆ•™™
777Ëÿ±£y&†Eãå1ÇCáQPP¿3œ<C@@ qqqLú8;;;ﬁx„ãÔDD‰ve~cSãà¸äÜRØ|ˇ˛˝?~‹Í5ŒŒŒLô2Ö¥¥4ñ,Ybµçøø?>¯ AAAçFNü>Õ˙ıÎmˆƒ–°CÒÒÒ·¸˘Û¨X±ÇÙÙÙzÌ	#55µﬁI√Ì⁄µ#<<ú]ªv]3o¿¡¡Å˚Ôøü»»HZ¥h¡Öÿπs'6l∞H™ı®˜ÑjsvÓ‹i~›ºysPØ›ñ-[0ƒƒƒ‘´€ºy≥Õ›†ˆLÜœŒl€∂ÕÊô
 ›∫u£}˚ˆı è9¬¡ÉÕØÉÉÉπˇ˛˚	†¢¢ÇÔæ˚éØæ˙äòòÛ9≈≈≈l⁄¥	®˝].[∂å˝˚˜3zÙh˙ˆÌKØ^Ωpww';;õÂÀó[$EDnG
DD§Iª:8xÍ©ßnˆpDDn*Âààààà†sDD§	ãää2n◊ºys¢¢¢»œœ'++ÎÊLD‰&—≤"i≤íììÎÌ:µvÌZ>˛¯„õ4"ëõK¡Åààààà  9ë:
DDDDDPp """""uààààà†‡@DDDDDÍ(8@¡Åààààà‘Qp """""ÄÇ©£‡@DDDDD """""RG¡Åààààà ˇ-7lı"kÿ    IENDÆB`Ç<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.38.0 (20140413.2041)
 -->
<!-- Title: %3 Pages: 1 -->
<svg width="581pt" height="355pt"
 viewBox="0.00 0.00 581.00 355.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 351)">
<title>%3</title>
<polygon fill="#333333" stroke="none" points="-4,4 -4,-351 577,-351 577,4 -4,4"/>
<text text-anchor="middle" x="286.5" y="-9.2" font-family="Times,serif" font-size="16.00" fill="white">Network Map</text>
<!-- SW1 -->
<g id="node1" class="node"><title>SW1</title>
<polygon fill="#006699" stroke="#006699" points="288,-99 196,-99 196,-26 288,-26 288,-99"/>
<text text-anchor="middle" x="242" y="-58.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">SW1</text>
</g>
<!-- R2 -->
<g id="node3" class="node"><title>R2</title>
<polygon fill="#006699" stroke="#006699" points="96.5,-223 19.5,-223 19.5,-150 96.5,-150 96.5,-223"/>
<text text-anchor="middle" x="58" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R2</text>
</g>
<!-- SW1&#45;&#45;R2 -->
<g id="edge2" class="edge"><title>SW1&#45;&#45;R2</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M195.85,-66.0313C157.833,-70.6235 105.266,-83.1667 74,-117 65.7944,-125.879 61.5425,-138.135 59.4135,-149.829"/>
<text text-anchor="middle" x="124" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="34.4135" y="-138.629" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="170.85" y="-54.8313" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/2</text>
</g>
<!-- R1 -->
<g id="node4" class="node"><title>R1</title>
<polygon fill="#006699" stroke="#006699" points="219.5,-223 142.5,-223 142.5,-150 219.5,-150 219.5,-223"/>
<text text-anchor="middle" x="181" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R1</text>
</g>
<!-- SW1&#45;&#45;R1 -->
<g id="edge1" class="edge"><title>SW1&#45;&#45;R1</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M195.881,-96.793C190.284,-102.865 185.364,-109.638 182,-117 177.403,-127.061 176.014,-138.852 176.109,-149.788"/>
<text text-anchor="middle" x="232" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="151.109" y="-138.588" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="170.881" y="-85.593" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
<!-- R6 -->
<g id="node7" class="node"><title>R6</title>
<polygon fill="#006699" stroke="#006699" points="342.5,-223 265.5,-223 265.5,-150 342.5,-150 342.5,-223"/>
<text text-anchor="middle" x="304" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R6</text>
</g>
<!-- SW1&#45;&#45;R6 -->
<g id="edge4" class="edge"><title>SW1&#45;&#45;R6</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M271.235,-99.2785C275.175,-105.007 278.915,-111.023 282,-117 287.27,-127.212 291.593,-138.931 294.97,-149.755"/>
<text text-anchor="middle" x="339" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="269.97" y="-138.555" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
<text text-anchor="middle" x="246.235" y="-103.079" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/5</text>
</g>
<!-- R3 -->
<g id="node8" class="node"><title>R3</title>
<polygon fill="#006699" stroke="#006699" points="465.5,-223 388.5,-223 388.5,-150 465.5,-150 465.5,-223"/>
<text text-anchor="middle" x="427" y="-182.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R3</text>
</g>
<!-- SW1&#45;&#45;R3 -->
<g id="edge3" class="edge"><title>SW1&#45;&#45;R3</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M288.272,-70.4405C320.828,-77.3989 363.655,-90.9867 393,-117 402.836,-125.719 410.149,-137.939 415.42,-149.648"/>
<text text-anchor="middle" x="456" y="-120.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="390.42" y="-138.448" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="313.272" y="-59.2405" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/3</text>
</g>
<!-- R5 -->
<g id="node2" class="node"><title>R5</title>
<polygon fill="#006699" stroke="#006699" points="403.5,-347 326.5,-347 326.5,-274 403.5,-274 403.5,-347"/>
<text text-anchor="middle" x="365" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R5</text>
</g>
<!-- SW2 -->
<g id="node6" class="node"><title>SW2</title>
<polygon fill="#006699" stroke="#006699" points="104,-347 12,-347 12,-274 104,-274 104,-347"/>
<text text-anchor="middle" x="58" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">SW2</text>
</g>
<!-- R2&#45;&#45;SW2 -->
<g id="edge5" class="edge"><title>R2&#45;&#45;SW2</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M58,-223.115C58,-239.01 58,-257.704 58,-273.629"/>
<text text-anchor="middle" x="108" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="29" y="-262.429" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/11</text>
<text text-anchor="middle" x="33" y="-226.915" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
<!-- R4 -->
<g id="node5" class="node"><title>R4</title>
<polygon fill="#006699" stroke="#006699" points="526.5,-347 449.5,-347 449.5,-274 526.5,-274 526.5,-347"/>
<text text-anchor="middle" x="488" y="-306.8" font-family="Helvetica,sans-Serif" font-size="14.00" fill="white">R4</text>
</g>
<!-- R3&#45;&#45;R5 -->
<g id="edge7" class="edge"><title>R3&#45;&#45;R5</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M388.218,-210.267C377.75,-218.511 367.74,-228.841 362,-241 357.274,-251.011 356.378,-262.789 357.152,-273.728"/>
<text text-anchor="middle" x="412" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="332.152" y="-262.528" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="363.218" y="-214.067" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/2</text>
</g>
<!-- R3&#45;&#45;R4 -->
<g id="edge6" class="edge"><title>R3&#45;&#45;R4</title>
<path fill="none" stroke="green" stroke-dasharray="5,2" d="M455.28,-223.045C459.199,-228.854 462.927,-234.955 466,-241 471.208,-251.244 475.514,-262.971 478.893,-273.794"/>
<text text-anchor="middle" x="523" y="-244.8" font-family="Courier,monospace" font-size="14.00" fill="white"> &#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;</text>
<text text-anchor="middle" x="453.893" y="-262.594" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/0</text>
<text text-anchor="middle" x="430.28" y="-226.845" font-family="Courier,monospace" font-size="14.00" fill="white">Eth0/1</text>
</g>
</g>
</svg>
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 11.4

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é create_network_map, –∫–æ—Ç–æ—Ä–∞—è –æ–±—Ä–∞–±–∞—Ç—ã–≤–∞–µ—Ç –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã show cdp
neighbors –∏–∑ –Ω–µ—Å–∫–æ–ª—å–∫–∏—Ö —Ñ–∞–π–ª–æ–≤ –∏ –æ–±—ä–µ–¥–∏–Ω—è–µ—Ç –µ–≥–æ –≤ –æ–¥–Ω—É –æ–±—â—É—é —Ç–æ–ø–æ–ª–æ–≥–∏—é.

–£ —Ñ—É–Ω–∫—Ü–∏–∏ –¥–æ–ª–∂–µ–Ω –±—ã—Ç—å –æ–¥–∏–Ω –ø–∞—Ä–∞–º–µ—Ç—Ä filenames, –∫–æ—Ç–æ—Ä—ã–π –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç
—Å–ø–∏—Å–æ–∫ —Å –∏–º–µ–Ω–∞–º–∏ —Ñ–∞–π–ª–æ–≤, –≤ –∫–æ—Ç–æ—Ä—ã—Ö –Ω–∞—Ö–æ–¥–∏—Ç—Å—è –≤—ã–≤–æ–¥ –∫–æ–º–∞–Ω–¥—ã show cdp neighbors.

–§—É–Ω–∫—Ü–∏—è –¥–æ–ª–∂–Ω–∞ –≤–æ–∑–≤—Ä–∞—â–∞—Ç—å —Å–ª–æ–≤–∞—Ä—å, –∫–æ—Ç–æ—Ä—ã–π –æ–ø–∏—Å—ã–≤–∞–µ—Ç —Å–æ–µ–¥–∏–Ω–µ–Ω–∏—è –º–µ–∂–¥—É
—É—Å—Ç—Ä–æ–π—Å—Ç–≤–∞–º–∏. –°—Ç—Ä—É–∫—Ç—É—Ä–∞ —Å–ª–æ–≤–∞—Ä—è —Ç–∞–∫–∞—è –∂–µ, –∫–∞–∫ –≤ –∑–∞–¥–∞–Ω–∏–∏ 11.3:
    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

C–≥–µ–Ω–µ—Ä–∏—Ä–æ–≤–∞—Ç—å —Ç–æ–ø–æ–ª–æ–≥–∏—é, –∫–æ—Ç–æ—Ä–∞—è —Å–æ–æ—Ç–≤–µ—Ç—Å—Ç–≤—É–µ—Ç –≤—ã–≤–æ–¥—É –∏–∑ —Ñ–∞–π–ª–æ–≤:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

–ù–µ –∫–æ–ø–∏—Ä–æ–≤–∞—Ç—å –∫–æ–¥ —Ñ—É–Ω–∫—Ü–∏–∏ parse_cdp_neighbors.
–ï—Å–ª–∏ —Ñ—É–Ω–∫—Ü–∏—è parse_cdp_neighbors –Ω–µ –º–æ–∂–µ—Ç –æ–±—Ä–∞–±–æ—Ç–∞—Ç—å –≤—ã–≤–æ–¥ –æ–¥–Ω–æ–≥–æ –∏–∑ —Ñ–∞–π–ª–æ–≤
—Å –≤—ã–≤–æ–¥–æ–º –∫–æ–º–∞–Ω–¥—ã, –Ω–∞–¥–æ –∏—Å–ø—Ä–∞–≤–∏—Ç—å –∫–æ–¥ —Ñ—É–Ω–∫—Ü–∏–∏ –≤ –∑–∞–¥–∞–Ω–∏–∏ 11.3.

–ü—Ä–∏–º–µ—Ä —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏
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
–ó–∞–≤–¥–∞–Ω–Ω—è 12.1

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é ping_ip_addresses, –∫–æ—Ç–æ—Ä–∞—è –ø—Ä–æ–≤–µ—Ä—è–µ—Ç –ø–∏–Ω–≥—É—é—Ç—Å—è –ª–∏ IP-–∞–¥—Ä–µ—Å–∞.

–§—É–Ω–∫—Ü–∏—è –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫ IP-–∞–¥—Ä–µ—Å–æ–≤.

–§—É–Ω–∫—Ü—ñ—è –º–∞—î –ø–æ–≤–µ—Ä—Ç–∞—Ç–∏ –∫–æ—Ä—Ç–µ–∂ —ñ–∑ –¥–≤–æ–º–∞ —Å–ø–∏—Å–∫–∞–º–∏:
* —Å–ø–∏—Å–æ–∫ –¥–æ—Å—Ç—É–ø–Ω—ã—Ö IP-–∞–¥—Ä–µ—Å–æ–≤
* —Å–ø–∏—Å–æ–∫ –Ω–µ–¥–æ—Å—Ç—É–ø–Ω—ã—Ö IP-–∞–¥—Ä–µ—Å–æ–≤

–î–ª—è –ø—Ä–æ–≤–µ—Ä–∫–∏ –¥–æ—Å—Ç—É–ø–Ω–æ—Å—Ç–∏ IP-–∞–¥—Ä–µ—Å–∞, –∏—Å–ø–æ–ª—å–∑—É–π—Ç–µ –∫–æ–º–∞–Ω–¥—É ping (–∑–∞–ø—É—Å–∫ ping —á–µ—Ä–µ–∑
subprocess).  IP-–∞–¥—Ä–µ—Å —Å—á–∏—Ç–∞–µ—Ç—Å—è –¥–æ—Å—Ç—É–ø–Ω—ã–º, –µ—Å–ª–∏ –≤—ã–ø–æ–ª–Ω–µ–Ω–∏–µ –∫–æ–º–∞–Ω–¥—ã ping
–æ—Ç—Ä–∞–±–æ—Ç–∞–ª–æ —Å –∫–æ–¥–æ–º 0 (returncode).  –ù—é–∞–Ω—Å—ã: –Ω–∞ Windows returncode –º–æ–∂–µ—Ç –±—ã—Ç—å
—Ä–∞–≤–µ–Ω 0 –Ω–µ —Ç–æ–ª—å–∫–æ, –∫–æ–≥–¥–∞ ping –±—ã–ª —É—Å–ø–µ—à–µ–Ω, –Ω–æ –¥–ª—è –∑–∞–¥–∞–Ω–∏—è –Ω—É–∂–Ω–æ –ø—Ä–æ–≤–µ—Ä—è—Ç—å
–∏–º–µ–Ω–Ω–æ –∫–æ–¥. –≠—Ç–æ —Å–¥–µ–ª–∞–Ω–æ –¥–ª—è —É–ø—Ä–æ—â–µ–Ω–∏—è —Ç–µ—Å—Ç–æ–≤.

"""
# -*- coding: utf-8 -*-
"""
–ó–∞–≤–¥–∞–Ω–Ω—è 12.2

–§—É–Ω–∫—Ü–∏—è ping_ip_addresses –∏–∑ –∑–∞–¥–∞–Ω–∏—è 12.1 –ø—Ä–∏–Ω–∏–º–∞–µ—Ç —Ç–æ–ª—å–∫–æ —Å–ø–∏—Å–æ–∫ –∞–¥—Ä–µ—Å–æ–≤,
–Ω–æ –±—ã–ª–æ –±—ã —É–¥–æ–±–Ω–æ –∏–º–µ—Ç—å –≤–æ–∑–º–æ–∂–Ω–æ—Å—Ç—å —É–∫–∞–∑—ã–≤–∞—Ç—å –∞–¥—Ä–µ—Å–∞ —Å –ø–æ–º–æ—â—å—é –¥–∏–∞–ø–∞–∑–æ–Ω–∞,
–Ω–∞–ø—Ä–∏–º–µ—Ä, 192.168.100.1-10.

–í —ç—Ç–æ–º –∑–∞–¥–∞–Ω–∏–∏ –Ω–µ–æ–±—Ö–æ–¥–∏–º–æ —Å–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é convert_ranges_to_ip_list,
–∫–æ—Ç–æ—Ä–∞—è –∫–æ–Ω–≤–µ—Ä—Ç–∏—Ä—É–µ—Ç —Å–ø–∏—Å–æ–∫ IP-–∞–¥—Ä–µ—Å–æ–≤ –≤ —Ä–∞–∑–Ω—ã—Ö —Ñ–æ—Ä–º–∞—Ç–∞—Ö –≤ —Å–ø–∏—Å–æ–∫,
–≥–¥–µ –∫–∞–∂–¥—ã–π IP-–∞–¥—Ä–µ—Å —É–∫–∞–∑–∞–Ω –æ—Ç–¥–µ–ª—å–Ω–æ.

–§—É–Ω–∫—Ü–∏—è –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç —Å–ø–∏—Å–æ–∫, –≤ –∫–æ—Ç–æ—Ä–æ–º —Å–æ–¥–µ—Ä–∂–∞—Ç—Å—è IP-–∞–¥—Ä–µ—Å–∞
–∏/–∏–ª–∏ –¥–∏–∞–ø–∞–∑–æ–Ω—ã IP-–∞–¥—Ä–µ—Å–æ–≤.

–≠–ª–µ–º–µ–Ω—Ç—ã —Å–ø–∏—Å–∫–∞ –º–æ–≥—É—Ç –±—ã—Ç—å –≤ —Ñ–æ—Ä–º–∞—Ç–µ:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

–ï—Å–ª–∏ –∞–¥—Ä–µ—Å —É–∫–∞–∑–∞–Ω –≤ –≤–∏–¥–µ –¥–∏–∞–ø–∞–∑–æ–Ω–∞, –Ω–∞–¥–æ —Ä–∞–∑–≤–µ—Ä–Ω—É—Ç—å –¥–∏–∞–ø–∞–∑–æ–Ω –≤ –æ—Ç–¥–µ–ª—å–Ω—ã–µ
–∞–¥—Ä–µ—Å–∞, –≤–∫–ª—é—á–∞—è –ø–æ—Å–ª–µ–¥–Ω–∏–π –∞–¥—Ä–µ—Å –¥–∏–∞–ø–∞–∑–æ–Ω–∞.
–î–ª—è —É–ø—Ä–æ—â–µ–Ω–∏—è –∑–∞–¥–∞—á–∏, –º–æ–∂–Ω–æ —Å—á–∏—Ç–∞—Ç—å, —á—Ç–æ –≤ –¥–∏–∞–ø–∞–∑–æ–Ω–µ –≤—Å–µ–≥–¥–∞ –º–µ–Ω—è–µ—Ç—Å—è —Ç–æ–ª—å–∫–æ
–ø–æ—Å–ª–µ–¥–Ω–∏–π –æ–∫—Ç–µ—Ç –∞–¥—Ä–µ—Å–∞.

–§—É–Ω–∫—Ü–∏—è –≤–æ–∑–≤—Ä–∞—â–∞–µ—Ç —Å–ø–∏—Å–æ–∫ IP-–∞–¥—Ä–µ—Å–æ–≤.

–ü—Ä–∏–º–µ—Ä –≤—ã–∑–æ–≤–∞ —Ñ—É–Ω–∫—Ü–∏–∏
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
–ó–∞–≤–¥–∞–Ω–Ω—è 12.3

–°–æ–∑–¥–∞—Ç—å —Ñ—É–Ω–∫—Ü–∏—é print_ip_table, –∫–æ—Ç–æ—Ä–∞—è –æ—Ç–æ–±—Ä–∞–∂–∞–µ—Ç —Ç–∞–±–ª–∏—Ü—É –¥–æ—Å—Ç—É–ø–Ω—ã—Ö
–∏ –Ω–µ–¥–æ—Å—Ç—É–ø–Ω—ã—Ö IP-–∞–¥—Ä–µ—Å–æ–≤.

–§—É–Ω–∫—Ü–∏—è –æ–∂–∏–¥–∞–µ—Ç –∫–∞–∫ –∞—Ä–≥—É–º–µ–Ω—Ç—ã –¥–≤–∞ —Å–ø–∏—Å–∫–∞:
* —Å–ø–∏—Å–æ–∫ –¥–æ—Å—Ç—É–ø–Ω—ã—Ö IP-–∞–¥—Ä–µ—Å–æ–≤
* —Å–ø–∏—Å–æ–∫ –Ω–µ–¥–æ—Å—Ç—É–ø–Ω—ã—Ö IP-–∞–¥—Ä–µ—Å–æ–≤

–†–µ–∑—É–ª—å—Ç–∞—Ç —Ä–∞–±–æ—Ç—ã —Ñ—É–Ω–∫—Ü–∏–∏ - –≤—ã–≤–æ–¥ –Ω–∞ —Å—Ç–∞–Ω–¥–∞—Ä—Ç–Ω—ã–π –ø–æ—Ç–æ–∫ –≤—ã–≤–æ–¥–∞ —Ç–∞–±–ª–∏—Ü—ã –≤–∏–¥–∞:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

–§—É–Ω–∫—Ü—ñ—è –Ω—ñ—á–æ–≥–æ –Ω–µ –ø–æ–≤–µ—Ä—Ç–∞—î, —Ç–æ–ª—å–∫–æ –¥–µ–ª–∞–µ—Ç print.

–ü—Ä–∏–º–µ—Ä –≤—ã–∑–æ–≤–∞ —Ñ—É–Ω–∫—Ü–∏–∏
In [6]: reach_ip = ["10.1.1.1", "10.1.1.2"]
In [7]: unreach_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]

In [8]: print_ip_table(reach_ip, unreach_ip)
Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
