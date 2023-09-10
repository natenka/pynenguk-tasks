import task_17_3
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_17_3, "parse_sh_cdp_neighbors")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    with open("sh_cdp_n_sw1.txt") as f:
        sh_cdp_n_sw1 = f.read()

    correct_return_value = {
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        }
    }

    return_value = task_17_3.parse_sh_cdp_neighbors(sh_cdp_n_sw1)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args():
    """
    Перевірка роботи функції
    """
    with open("sh_cdp_n_sw1.txt") as f:
        sh_cdp_n_sw1 = f.read()

    correct_return_value = {
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        }
    }

    return_value = task_17_3.parse_sh_cdp_neighbors(sh_cdp_n_sw1)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
