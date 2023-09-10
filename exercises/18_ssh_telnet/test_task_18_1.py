import task_18_1
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_1, "send_show_command")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_command("sh ip int br")
    )
    return_value = strip_empty_lines(
        task_18_1.send_show_command(first_router_from_devices_yaml, "sh ip int br")
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
    correct_return_value = strip_empty_lines(
        r1_test_connection.send_command("sh int description")
    )
    return_value = strip_empty_lines(
        task_18_1.send_show_command(
            first_router_from_devices_yaml, "sh int description"
        )
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, str):
        pytest.fail(
            f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
