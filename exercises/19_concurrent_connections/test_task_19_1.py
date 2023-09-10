import task_19_1
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, get_reach_unreach


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_19_1, "ping_ip_addresses")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "2.2.2.2"]
    correct_return_value = get_reach_unreach(list_of_ips)
    correct_reachable, correct_unreachable = correct_return_value
    correct_reachable, correct_unreachable = sorted(correct_reachable), sorted(
        correct_unreachable
    )

    return_value = task_19_1.ping_ip_addresses(list_of_ips)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    assert (
        type(return_value) == tuple
    ), f"За завданням функція має повертати кортеж, а повертає {type(return_value).__name__}"
    assert 2 == len(return_value), "Функція має повертати кортеж із двома списками"
    assert all(
        type(item) == list for item in return_value
    ), "Функція повинна повертати кортеж зі списками усередині"

    return_reachable, return_unreachable = return_value
    return_reachable, return_unreachable = sorted(return_reachable), sorted(
        return_unreachable
    )
    assert correct_return_value == (
        return_value
    ), "Функція повертає неправильне значення"
