import task_15_2
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_15_2, "parse_sh_ip_int_br")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        ("FastEthernet0/0", "15.0.15.1", "up", "up"),
        ("FastEthernet0/1", "10.0.12.1", "up", "up"),
        ("FastEthernet0/2", "10.0.13.1", "up", "up"),
        ("FastEthernet0/3", "unassigned", "administratively down", "down"),
        ("Loopback0", "10.1.1.1", "up", "up"),
        ("Loopback100", "100.0.0.1", "up", "up"),
    ]

    return_value = task_15_2.parse_sh_ip_int_br("sh_ip_int_br.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Функція повертає неправильне значення"


def test_function_return_value_different_args():
    """
    Перевірка роботи функції з іншими аргументами
    """
    correct_return_value = [
        ("FastEthernet0/0", "15.0.15.2", "up", "up"),
        ("FastEthernet0/1", "10.0.12.2", "up", "up"),
        ("FastEthernet0/2", "10.0.13.2", "down", "down"),
        ("FastEthernet0/3", "unassigned", "administratively down", "down"),
        ("Loopback0", "10.2.2.2", "up", "up"),
    ]

    return_value = task_15_2.parse_sh_ip_int_br("sh_ip_int_br_2.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Функція повертає неправильне значення"
