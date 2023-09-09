import os
import task_20_5
import sys

sys.path.append("..")

from pyneng_common_functions import strip_empty_lines


def test_templates_exists():
    assert os.path.exists(
        "templates/gre_ipsec_vpn_1.txt"
    ), "Шаблон templates/gre_ipsec_vpn_1.txt не існує"
    assert os.path.exists(
        "templates/gre_ipsec_vpn_2.txt"
    ), "Шаблон templates/gre_ipsec_vpn_2.txt не існує"


def test_function_return_value():
    data = {
        "tun_num": 17,
        "wan_ip_1": "80.241.1.1",
        "wan_ip_2": "90.18.10.2",
        "tun_ip_1": "10.255.1.1 255.255.255.252",
        "tun_ip_2": "10.255.1.2 255.255.255.252",
    }
    correct_value_1 = (
        "interface Tunnel 17\n"
        "ip address 10.255.1.1 255.255.255.252\n"
        "tunnel source 80.241.1.1\n"
        "tunnel destination 90.18.10.2\n"
        "tunnel protection ipsec profile GRE"
    )
    correct_value_2 = (
        "interface Tunnel 17\n"
        "ip address 10.255.1.2 255.255.255.252\n"
        "tunnel source 90.18.10.2\n"
        "tunnel destination 80.241.1.1\n"
        "tunnel protection ipsec profile GRE"
    )

    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"

    return_cfg1, return_cfg2 = task_20_5.create_vpn_config(template1, template2, data)
    return_cfg1 = strip_empty_lines(return_cfg1)
    return_cfg2 = strip_empty_lines(return_cfg2)

    assert (
        correct_value_1 in return_cfg1
    ), "У підсумковій конфігурації неправильно вказано налаштування Tunnel для першої сторони"
    assert (
        correct_value_2 in return_cfg2
    ), "У підсумковій конфігурації неправильно вказано налаштування Tunnel для другої сторони"
