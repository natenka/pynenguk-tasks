# -*- coding: utf-8 -*-
"""
Завдання 5.4a

Запросити користувача введення IP-мережі у форматі: 10.1.1.0 255.255.255.0

Потім вивести інформацію про мережу та маску в такому форматі:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Перевірити роботу скрипта на різних комбінаціях мережа/маска.

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Приклад роботи завдання:

$ python task_5_4a.py
Enter network address: 10.1.1.0 255.255.255.0

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


$ python task_5_4a.py
Enter network address: 10.1.1.192 255.255.255.240

Network:
10        1         1         192
00001010  00000001  00000001  11000000

Mask:
/28
255       255       255       240
11111111  11111111  11111111  11110000
"""

# -*- coding: utf-8 -*-


network = input("Enter network address: ")

ip, mask = network.split()
ip_list = ip.split(".")
mask_list = mask.split(".")

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]

m1, m2, m3, m4 = [
    int(mask_list[0]),
    int(mask_list[1]),
    int(mask_list[2]),
    int(mask_list[3]),
]
bin_mask = "{:08b}{:08b}{:08b}{:08b}".format(m1, m2, m3, m4)
mask = bin_mask.count("1")

ip_output = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

mask_output = """
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
"""

print(ip_output.format(oct1, oct2, oct3, oct4))
print(mask_output.format(mask, m1, m2, m3, m4))
