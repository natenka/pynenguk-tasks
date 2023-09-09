import pytest
import task_12_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, get_reach_unreach


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_12_1, "ping_ip_addresses")


@pytest.mark.skipif(
    not hasattr(task_12_1, "ping_ip_addresses"),
    reason="Этот тест работает только если создана функция ping_ip_addresses",
)
def test_function_return_value():
    """
    Перевірка роботи функції
    """
    list_of_ips = ["1.1.1.1", "8.8.8.8", "8.8.4.4", "8.8.7.1"]
    correct_return_value = get_reach_unreach(list_of_ips)

    return_value = task_12_1.ping_ip_addresses(list_of_ips)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    assert type(return_value) == tuple and all(
        type(item) == list for item in return_value
    ), "Функція має повертати кортеж із двома списками"
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
