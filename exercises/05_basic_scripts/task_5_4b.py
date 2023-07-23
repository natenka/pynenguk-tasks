# -*- coding: utf-8 -*-
"""
Завдання 5.4b

Все, як у завданні 5.4a, але, якщо користувач ввів адресу хоста, а не адресу
мережі, треба перетворити адресу хоста на адресу мережі та вивести адресу
мережі та маску, як у завданні 5.4a.

Приклад адреси мережі (усі біти хостової частини дорівнюють нулю):
* 10.0.1.0 255.255.255.0
* 190.1.0.0 255.255.0.0

Приклад адреси хоста:
* 10.0.1.1 255.255.255.0 - хост із мережі 10.0.1.0 255.255.255.0
* 10.0.5.195 255.255.255.240 - хост із мережі 10.0.5.192 255.255.255.240

Приклад роботи завдання якщо користувач ввів адресу 10.0.1.1 255.255.255.0,

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Перевірити роботу скрипту на різних комбінаціях хост/маска, наприклад:
    10.0.5.195 255.255.255.240, 10.0.1.1 255.255.255.0

Вивід має бути впорядкований як у прикладі:
* стовпцями
* ширина стовпця 10 символів (у двійковому форматі треба додати два пробіли між
  стовпцями для поділу октетів між собою)

Підказка: наприклад є адреса хоста у двійковому форматі та маска мережі 28.
Адреса мережі це перші 28 біт адреси хоста + 4 нуля. Тобто, наприклад, адреса
хоста 10.1.1.195/28 у двійковому форматі буде
bin_ip = "0000101000000001000000111000011"

А адреса мережі буде перших 28 символів з bin_ip + 0000 (4 тому що всього в
адресі може бути 32 біти, а 32 - 28 = 4)
00001010000000010000000111000000
"""
# -*- coding: utf-8 -*-

network = input("Enter host address: ")

ip, mask = network.split()
ip_list = ip.split(".")
mask_list = mask.split(".")
m1, m2, m3, m4 = [
    int(mask_list[0]),
    int(mask_list[1]),
    int(mask_list[2]),
    int(mask_list[3]),
]
bin_mask = "{:08b}{:08b}{:08b}{:08b}".format(m1, m2, m3, m4)
mask = int(bin_mask.count("1"))

oct1, oct2, oct3, oct4 = [
    int(ip_list[0]),
    int(ip_list[1]),
    int(ip_list[2]),
    int(ip_list[3]),
]
bin_ip_str = "{:08b}{:08b}{:08b}{:08b}".format(oct1, oct2, oct3, oct4)
bin_network_str = bin_ip_str[:mask] + "0" * (32 - mask)

net1, net2, net3, net4 = [
    int(bin_network_str[0:8], 2),
    int(bin_network_str[8:16], 2),
    int(bin_network_str[16:24], 2),
    int(bin_network_str[24:32], 2),
]

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

print(ip_output.format(net1, net2, net3, net4))
print(mask_output.format(mask, m1, m2, m3, m4))
