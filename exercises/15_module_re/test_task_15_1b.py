import task_15_1b
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_15_1b, "get_ip_from_cfg")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = {
        "Loopback0": [("10.2.2.2", "255.255.255.255")],
        "Ethernet0/0": [("10.0.23.2", "255.255.255.0")],
        "Ethernet0/1": [
            ("10.255.2.2", "255.255.255.0"),
            ("10.254.2.2", "255.255.255.0"),
        ],
        "Ethernet0/2": [("10.0.29.2", "255.255.255.0")],
    }

    return_value = task_15_1b.get_ip_from_cfg("config_r2.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
