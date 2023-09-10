import task_9_3a
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_3a, "clean_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_3a.clean_config,
        param_count=5,
        param_names=[
            "config_filename",
            "ignore_lines",
            "ignore_exclamation",
            "strip_lines",
            "delete_empty_lines",
        ],
    )


def test_function_return_value_ignore_list():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "hostname PE_r3",
        "!",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "!",
        "!",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "!",
        "!",
        "!",
        "alias configure sh do sh",
        "!",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
    return_value = task_9_3a.clean_config(
        "config_r3_short.txt",
        strip_lines=True,
        ignore_lines=ignore_list,
        ignore_exclamation=False,
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args_1():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "hostname PE_r3",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "alias configure sh do sh",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
    return_value = task_9_3a.clean_config(
        "config_r3_short.txt", strip_lines=True, ignore_lines=ignore_list
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_args_2():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "hostname PE_r3",
        "",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "",
        "alias configure sh do sh",
        "alias exec ospf sh run | s ^router ospf",
        "alias exec bri show ip int bri | exc unass",
        "line con 0",
        "exec-timeout 0 0",
        "privilege level 15",
        "logging synchronous",
    ]

    return_value = task_9_3a.clean_config(
        "config_r3_short.txt", strip_lines=True, delete_empty_lines=False
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
