import os
import re
import task_20_5a
import sys

sys.path.append("..")


def get_interface_cfg(cfg_output):
    interface_cfg = []
    for line in cfg_output.splitlines():
        if "(config-if)" in line:
            interface_cfg.append(re.sub(r"\S+\(config-if\)# *", "", line))
    return "\n".join(interface_cfg)


def test_templates_exists():
    assert os.path.exists(
        "templates/gre_ipsec_vpn_1.txt"
    ), "Шаблон templates/gre_ipsec_vpn_1.txt не існує"
    assert os.path.exists(
        "templates/gre_ipsec_vpn_2.txt"
    ), "Шаблон templates/gre_ipsec_vpn_2.txt не існує"


def test_function_return_value(first_two_routers_from_devices_yaml):
    r1, r2 = first_two_routers_from_devices_yaml
    data = {
        "tun_num": None,
        "wan_ip_1": "80.241.1.1",
        "wan_ip_2": "90.18.10.2",
        "tun_ip_1": "10.255.1.1 255.255.255.252",
        "tun_ip_2": "10.255.1.2 255.255.255.252",
    }
    correct_intf_1 = (
        "ip address 10.255.1.1 255.255.255.252\n"
        "tunnel source 80.241.1.1\n"
        "tunnel destination 90.18.10.2\n"
        "tunnel protection ipsec profile GRE"
    )
    correct_intf_2 = (
        "ip address 10.255.1.2 255.255.255.252\n"
        "tunnel source 90.18.10.2\n"
        "tunnel destination 80.241.1.1\n"
        "tunnel protection ipsec profile GRE"
    )

    template1 = "templates/gre_ipsec_vpn_1.txt"
    template2 = "templates/gre_ipsec_vpn_2.txt"

    return_value = task_20_5a.configure_vpn(r1, r2, template1, template2, data)
    return_cfg1, return_cfg2 = return_value
    return_intf_cfg1 = get_interface_cfg(return_cfg1)
    return_intf_cfg2 = get_interface_cfg(return_cfg2)

    assert (
        type(return_value) == tuple
    ), f"За завданням функція має повертати кортеж, а повертає {type(return_value).__name__}"
    assert 2 == len(return_value) and all(
        type(item) == str for item in return_value
    ), "Функція має повертати кортеж із двома рядками"
    assert (
        correct_intf_1 in return_intf_cfg1
    ), "У підсумковій конфігурації неправильно вказано налаштування Tunnel для першої сторони"
    assert (
        correct_intf_2 in return_intf_cfg2
    ), "У підсумковій конфігурації неправильно вказано налаштування Tunnel для другої сторони"
