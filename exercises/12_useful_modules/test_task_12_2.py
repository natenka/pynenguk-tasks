import task_12_2
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_12_2, "convert_ranges_to_ip_list")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    list_of_ips_and_ranges = ["8.8.4.4", "1.1.1.1-3", "172.21.41.128-172.21.41.132"]
    correct_return_value = [
        "8.8.4.4",
        "1.1.1.1",
        "1.1.1.2",
        "1.1.1.3",
        "172.21.41.128",
        "172.21.41.129",
        "172.21.41.130",
        "172.21.41.131",
        "172.21.41.132",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
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
    Перевірка роботи функції на інших адресах
    """
    list_of_ips_and_ranges = ["10.1.1.1", "10.4.10.10-13", "192.168.1.12-192.168.1.15"]
    correct_return_value = [
        "10.1.1.1",
        "10.4.10.10",
        "10.4.10.11",
        "10.4.10.12",
        "10.4.10.13",
        "192.168.1.12",
        "192.168.1.13",
        "192.168.1.14",
        "192.168.1.15",
    ]

    return_value = task_12_2.convert_ranges_to_ip_list(list_of_ips_and_ranges)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert sorted(correct_return_value) == sorted(
        return_value
    ), "Функція повертає неправильне значення"
