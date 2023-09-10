import task_18_2
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_2, "send_config_commands")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Перевірка роботи функції
    """
    test_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_config_set(test_commands)
    )
    return_value = strip_empty_lines(
        task_18_2.send_config_commands(first_router_from_devices_yaml, test_commands)
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, str):
        pytest.fail(
            f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args(
    r1_test_connection, first_router_from_devices_yaml
):
    """
    Перевірка роботи функції с другими аргументами
    """
    test_commands = [
        "interface Loopback 100",
        "ip address 10.1.1.100 255.255.255.255",
    ]
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_config_set(test_commands)
    )
    return_value = strip_empty_lines(
        task_18_2.send_config_commands(first_router_from_devices_yaml, test_commands)
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, str):
        pytest.fail(
            f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
