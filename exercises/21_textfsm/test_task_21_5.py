import textfsm
import pytest
import os
import task_21_5
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_21_5, "send_and_parse_command_parallel")


def test_function_return_value(r1_test_connection, first_router_from_devices_yaml):
    """
    Перевірка роботи функції
    """
    with open("templates/sh_ip_int_br.template") as f:
        re_table = textfsm.TextFSM(f)
    sh_ip_int_br = r1_test_connection.send_command("sh ip int br")
    result = re_table.ParseText(sh_ip_int_br)
    correct_return_value = {
        first_router_from_devices_yaml["host"]: [
            dict(zip(re_table.header, line)) for line in result
        ]
    }

    full_pth = os.path.join(os.getcwd(), "templates")
    return_value = task_21_5.send_and_parse_command_parallel(
        [first_router_from_devices_yaml], "sh ip int br", templates_path=full_pth
    )

    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
