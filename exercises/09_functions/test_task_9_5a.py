import task_9_5a
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_5a, "generate_trunk_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_5a.generate_trunk_config,
        param_count=2,
        param_names=["intf_vlan_dict", "trunk_template"],
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    trunk_vlans_mapping = {
        "FastEthernet0/1": [10, 20, 30],
        "FastEthernet0/2": [11, 30],
        "FastEthernet0/4": [17],
    }
    template_trunk_mode = [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan",
    ]
    correct_return_value = {
        "FastEthernet0/1": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 10,20,30",
        ],
        "FastEthernet0/2": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 11,30",
        ],
        "FastEthernet0/4": [
            "switchport mode trunk",
            "switchport trunk native vlan 999",
            "switchport trunk allowed vlan 17",
        ],
    }

    return_value = task_9_5a.generate_trunk_config(
        trunk_vlans_mapping, template_trunk_mode
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
