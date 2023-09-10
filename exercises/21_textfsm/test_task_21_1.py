import task_21_1
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_21_1, "parse_command_output")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        ["intf", "address", "status", "protocol"],
        ["FastEthernet0/0", "15.0.15.1", "up", "up"],
        ["FastEthernet0/1", "10.0.12.1", "up", "up"],
        ["FastEthernet0/2", "10.0.13.1", "up", "up"],
        ["FastEthernet0/3", "unassigned", "up", "up"],
        ["Loopback0", "10.1.1.1", "up", "up"],
        ["Loopback100", "100.0.0.1", "up", "up"],
    ]
    with open("output/sh_ip_int_br.txt") as f:
        sh_ip_int_br = f.read()
    template = "templates/sh_ip_int_br.template"

    return_value = task_21_1.parse_command_output(template, sh_ip_int_br)
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
    correct_return_value = [
        ["network", "mask", "distance", "metric", "nexthop"],
        ["10.0.24.0", "24", "110", "20", ["10.0.12.2"]],
        ["10.0.34.0", "24", "110", "20", ["10.0.13.3"]],
        ["10.2.2.2", "32", "110", "11", ["10.0.12.2"]],
        ["10.3.3.3", "32", "110", "11", ["10.0.13.3"]],
        ["10.4.4.4", "32", "110", "21", ["10.0.13.3", "10.0.12.2", "10.0.14.4"]],
        ["10.5.35.0", "24", "110", "20", ["10.0.13.3"]],
    ]

    with open("output/sh_ip_route_ospf.txt") as f:
        sh_ip_int_br = f.read()
    template = "templates/sh_ip_route_ospf.template"

    return_value = task_21_1.parse_command_output(template, sh_ip_int_br)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
