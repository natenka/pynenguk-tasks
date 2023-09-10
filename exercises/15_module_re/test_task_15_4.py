import task_15_4
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_15_4, "get_ints_without_description")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "Loopback0",
        "Tunnel0",
        "Ethernet0/1",
        "Ethernet0/3.100",
        "Ethernet1/0",
    ]
    return_value = task_15_4.get_ints_without_description("config_r1.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Функція повертає неправильне значення"
