import os
import task_17_3b
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, unify_topology_dict


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_17_3b, "transform_topology")


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    correct_return_value = unify_topology_dict(
        {
            ("R1", "Eth 0/0"): ("SW1", "Eth 0/1"),
            ("R2", "Eth 0/0"): ("SW1", "Eth 0/2"),
            ("R2", "Eth 0/1"): ("R5", "Eth 0/0"),
            ("R2", "Eth 0/2"): ("R6", "Eth 0/1"),
            ("R3", "Eth 0/0"): ("SW1", "Eth 0/3"),
            ("R4", "Eth 0/0"): ("SW1", "Eth 0/4"),
            ("R4", "Eth 0/1"): ("R5", "Eth 0/1"),
        }
    )

    assert os.path.exists("topology.yaml"), "Файл topology.yaml не існує"
    return_value = task_17_3b.transform_topology("topology.yaml")
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert len(correct_return_value) == len(
        return_value
    ), "У словнику, який описує топологію є лінки, що дублюються"
    assert correct_return_value == unify_topology_dict(
        return_value
    ), "Функція повертає неправильне значення"
