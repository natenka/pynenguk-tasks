import task_11_4
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
)


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_11_4, "create_network_map")


def test_function_params():
    """
    Перевірка імен та кількості параметрів
    """
    check_function_params(
        function=task_11_4.create_network_map, param_count=1, param_names=["filenames"]
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
        ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
    }

    return_value = task_11_4.create_network_map(
        ["sh_cdp_n_r2.txt", "sh_cdp_n_r1.txt", "sh_cdp_n_sw1.txt", "sh_cdp_n_r3.txt"]
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
