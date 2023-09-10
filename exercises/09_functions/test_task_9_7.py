import task_9_7
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_7, "convert_config_to_dict")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_7.convert_config_to_dict,
        param_count=2,
        param_names=["config_filename", "ignore_lines"],
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = {
        "version 15.0": [],
        "service timestamps debug datetime msec": [],
        "service timestamps log datetime msec": [],
        "no service password-encryption": [],
        "hostname sw1": [],
        "interface FastEthernet0/0": [
            "switchport mode access",
            "switchport access vlan 10",
        ],
        "interface FastEthernet0/1": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,200",
            "switchport mode trunk",
        ],
        "interface FastEthernet0/2": [
            "switchport mode access",
            "switchport access vlan 20",
        ],
        "interface FastEthernet0/3": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,300,400,500,600",
            "switchport mode trunk",
        ],
        "interface FastEthernet1/0": [
            "switchport mode access",
            "switchport access vlan 20",
        ],
        "interface FastEthernet1/1": [
            "switchport mode access",
            "switchport access vlan 30",
        ],
        "interface FastEthernet1/2": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 400,500,600",
            "switchport mode trunk",
        ],
        "interface Vlan100": ["ip address 10.0.100.1 255.255.255.0"],
        "line con 0": ["exec-timeout 0 0", "privilege level 15", "logging synchronous"],
        "line aux 0": [],
        "line vty 0 4": ["login", "transport input all"],
        "end": [],
    }

    ignore = ["duplex", "alias", "configuration"]
    return_value = task_9_7.convert_config_to_dict(
        "config_sw1.txt", ignore_lines=ignore
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
