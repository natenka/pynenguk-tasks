import pytest
import task_18_3
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    strip_empty_lines,
)


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_3, "send_commands")


def test_function_params(r1_test_connection, first_router_from_devices_yaml):
    show_command = "sh ip int br"
    cfg_commands = ["logging buffered 20010"]
    with pytest.raises(TypeError) as excinfo:
        task_18_3.send_commands(first_router_from_devices_yaml, show_command)

    with pytest.raises(ValueError) as excinfo:
        task_18_3.send_commands(
            first_router_from_devices_yaml, show=show_command, config=cfg_commands
        )


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Перевірка роботи функції
    """
    show_command = "sh ip int br"
    cfg_commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    correct_return_value_show = strip_empty_lines(
        r1_test_connection.send_command(show_command)
    )
    correct_return_value_cfg = strip_empty_lines(
        r1_test_connection.send_config_set(cfg_commands)
    )
    return_value_show = strip_empty_lines(
        task_18_3.send_commands(first_router_from_devices_yaml, show=show_command)
    )
    return_value_cfg = strip_empty_lines(
        task_18_3.send_commands(first_router_from_devices_yaml, config=cfg_commands)
    )
    assert return_value_show != None, "Функція нічого не повертає"
    assert (
        type(return_value_show) == str
    ), f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
    assert (
        correct_return_value_show == return_value_show
    ), "Функція повертає неправильне значення при передачі команди show"
    assert (
        correct_return_value_cfg == return_value_cfg
    ), "Функція повертає неправильне значення під час передачі конфігураційних команд"
