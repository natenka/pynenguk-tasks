import task_15_5
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_15_5, "generate_description_from_cdp")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = {
        "Eth 0/1": "description Connected to R1 port Eth 0/0",
        "Eth 0/2": "description Connected to R2 port Eth 0/0",
        "Eth 0/3": "description Connected to R3 port Eth 0/0",
        "Eth 0/5": "description Connected to R6 port Eth 0/1",
    }
    return_value = task_15_5.generate_description_from_cdp("sh_cdp_n_sw1.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
