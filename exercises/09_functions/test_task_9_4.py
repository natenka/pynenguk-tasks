import task_9_4
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_4, "generate_access_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_4.generate_access_config,
        param_count=2,
        param_names=["intf_vlan_dict", "access_template"],
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    access_vlans_mapping = {
        "FastEthernet0/12": 10,
        "FastEthernet0/14": 11,
        "FastEthernet0/16": 17,
    }
    template_access_mode = [
        "switchport mode access",
        "switchport access vlan",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]
    correct_return_value = [
        "interface FastEthernet0/12",
        "switchport mode access",
        "switchport access vlan 10",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/14",
        "switchport mode access",
        "switchport access vlan 11",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
        "interface FastEthernet0/16",
        "switchport mode access",
        "switchport access vlan 17",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ]

    return_value = task_9_4.generate_access_config(
        access_vlans_mapping, template_access_mode
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args():
    """
    Перевірка роботи функції с другими аргументами
    """
    access_vlans_mapping = {
        "FastEthernet0/1": 101,
        "FastEthernet0/4": 121,
    }
    template_access_mode = [
        "switchport mode access",
        "switchport access vlan",
    ]
    correct_return_value = [
        "interface FastEthernet0/1",
        "switchport mode access",
        "switchport access vlan 101",
        "interface FastEthernet0/4",
        "switchport mode access",
        "switchport access vlan 121",
    ]

    return_value = task_9_4.generate_access_config(
        access_vlans_mapping, template_access_mode
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
