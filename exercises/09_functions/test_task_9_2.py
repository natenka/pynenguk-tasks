import task_9_2
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_2, "check_ip")


@pytest.mark.parametrize(
    "ip_address",
    ["10.1.1.250", "120.1.105.1", "130.150.1.1", "150.1.1.1"],
)
def test_task_correct_ip(ip_address):
    """
    Перевірка роботи завдання
    """
    return_value = task_9_2.check_ip(ip_address)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, bool):
        pytest.fail(
            f"За завданням функція має повертати True чи False, а повертає {type(return_value).__name__}"
        )
    assert True == return_value, "Функція повертає неправильне значення"


@pytest.mark.parametrize(
    "ip_address",
    ["10.1.1", "10.a.2.a", "10.1.1.1.1", "10.1.1.", "300.1.1.1", "30,1.1.1.1"],
)
def test_task_wrong_ip(ip_address):
    return_value = task_9_2.check_ip(ip_address)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, bool):
        pytest.fail(
            f"За завданням функція має повертати True чи False, а повертає {type(return_value).__name__}"
        )
    assert False == return_value, "Функція повертає неправильне значення"
