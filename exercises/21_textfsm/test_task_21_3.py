import task_21_3
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_21_3, "parse_command_dynamic")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        {
            "address": "15.0.15.1",
            "intf": "FastEthernet0/0",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.12.1",
            "intf": "FastEthernet0/1",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "10.0.13.1",
            "intf": "FastEthernet0/2",
            "protocol": "up",
            "status": "up",
        },
        {
            "address": "unassigned",
            "intf": "FastEthernet0/3",
            "protocol": "up",
            "status": "up",
        },
        {"address": "10.1.1.1", "intf": "Loopback0", "protocol": "up", "status": "up"},
        {
            "address": "100.0.0.1",
            "intf": "Loopback100",
            "protocol": "up",
            "status": "up",
        },
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}

    return_value = task_21_3.parse_command_dynamic(sh_ip_int_br, attributes)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args():
    correct_return_value = [
        {
            "hostname": "R1_LONDON",
            "version": "15.3(2)S1",
        }
    ]
    with open("output/sh_version.txt") as f:
        sh_version = f.read()
    attributes = {"Command": "show version", "Vendor": "cisco_ios"}

    return_value = task_21_3.parse_command_dynamic(sh_version, attributes)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
