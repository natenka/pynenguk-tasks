# -*- coding: utf-8 -*-
"""
Завдання 20.3

Створіть шаблон templates/ospf.txt на основі конфігурації OSPF у файлі
cisco_ospf.txt (це просто приклад конфігурації).

Шаблон треба створювати вручну. Це завдання на синтаксис шаблонів Jinja2.

Які значення мають бути змінними:

* номер процесу. Ім'я змінної - process
* router-id. Ім'я змінної – router_id
* reference-bandwidth. Ім'я змінної - ref_bw
* інтерфейси, у яких потрібно включити OSPF. Ім'я змінної – ospf_intf. На місці
  цієї змінної очікується список словників із такими ключами:
   * name - ім'я інтерфейсу, виду Fa0/1, Vlan10, Gi0/0
   * ip - IP-адреса інтерфейсу, виду 10.0.1.1
   * area - номер зони
   * passive – чи є інтерфейс пасивним. Допустимі значення: True або False

Для всіх інтерфейсів у списку ospf_intf, треба згенерувати рядки:
 network xxxx 0.0.0.0 area x

Якщо пасивний інтерфейс, для нього повинен бути доданий рядок:
 passive-interface x

Для інтерфейсів, які не є пасивними, в режимі конфігурації інтерфейсу треба додати рядок:
 ip ospf hello-interval 1

Усі команди мають бути у відповідних режимах.

Перевірте шаблон templates/ospf.txt, на даних у файлі data_files/ospf.yml, за
допомогою функції generate_config із завдання 20.1. Не копіюйте код функції
generate_config.

В результаті має вийти конфігурація такого виду (команди в режимі router ospf не
обов'язково повинні бути в такому порядку, головне щоб вони були в потрібному
режимі):

router ospf 10
 router-id 10.0.0.1
 auto-cost reference-bandwidth 20000
 network 10.255.0.1 0.0.0.0 area 0
 network 10.255.1.1 0.0.0.0 area 0
 network 10.255.2.1 0.0.0.0 area 0
 network 10.0.10.1 0.0.0.0 area 2
 network 10.0.20.1 0.0.0.0 area 2
 passive-interface Fa0/0.10
 passive-interface Fa0/0.20
interface Fa0/1
 ip ospf hello-interval 1
interface Fa0/1.100
 ip ospf hello-interval 1
interface Fa0/1.200
 ip ospf hello-interval 1
"""
