import task_15_1
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_15_1, "get_ip_from_cfg")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        ("10.1.1.1", "255.255.255.255"),
        ("10.0.13.1", "255.255.255.0"),
        ("10.0.19.1", "255.255.255.0"),
    ]

    return_value = task_15_1.get_ip_from_cfg("config_r1.txt")
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
        ("10.3.3.3", "255.255.255.255"),
        ("10.0.13.3", "255.255.255.0"),
    ]

    return_value = task_15_1.get_ip_from_cfg("config_r3.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Функція повертає неправильне значення"
