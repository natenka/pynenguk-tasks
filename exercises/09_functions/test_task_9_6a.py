import task_9_6a
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_6a, "get_int_vlan_map")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_6a.get_int_vlan_map,
        param_count=1,
        param_names=["config_filename"],
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = (
        {
            "FastEthernet0/0": 10,
            "FastEthernet0/2": 20,
            "FastEthernet1/0": 20,
            "FastEthernet1/1": 30,
            "FastEthernet1/3": 1,
            "FastEthernet2/0": 1,
            "FastEthernet2/1": 1,
        },
        {
            "FastEthernet0/1": [100, 200],
            "FastEthernet0/3": [100, 300, 400, 500, 600],
            "FastEthernet1/2": [400, 500, 600],
        },
    )

    return_value = task_9_6a.get_int_vlan_map("config_sw2.txt")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, tuple):
        pytest.fail(
            f"За завданням функція має повертати кортеж, а повертає {type(return_value).__name__}"
        )
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функція має повертати кортеж із двома словниками"
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
