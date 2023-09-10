import task_9_3
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_9_3, "clean_config")


def test_function_params():
    """
    Проверка имен и количества параметров
    """
    check_function_params(
        function=task_9_3.clean_config,
        param_count=2,
        param_names=["config_filename", "ignore_lines"],
    )


def test_function_return_value_ignore_list():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "version 15.2",
        "hostname PE_r2",
        "no ip http server",
        "no ip http secure-server",
        "ip route 10.2.2.2 255.255.255.255 Tunnel0",
        "ip access-list standard LDP",
        " deny   10.0.0.0 0.0.255.255",
        " permit 10.0.0.0 0.255.255.255",
        "ip prefix-list TEST seq 5 permit 10.6.6.6/32",
        "mpls ldp router-id Loopback0 force",
        "control-plane",
        "alias configure sh do sh",
        "line con 0",
        " exec-timeout 0 0",
        " privilege level 15",
        " logging synchronous",
        "line aux 0",
        "line vty 0 4",
        " login",
        " transport input all",
    ]

    ignore_list = ["duplex", "alias exec", "Current configuration", "service"]
    return_value = task_9_3.clean_config("config_r2_short.txt", ignore_list)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_ignore_lines_1():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "Current configuration : 4052 bytes",
        "version 15.2",
        "hostname PE_r2",
        " deny   10.0.0.0 0.0.255.255",
        " permit 10.0.0.0 0.255.255.255",
        "mpls ldp router-id Loopback0 force",
        "control-plane",
        "alias configure sh do sh",
        "alias exec ospf sh run | s ^router ospf",
        "alias exec id show int desc",
        " exec-timeout 0 0",
        " privilege level 15",
        " logging synchronous",
        " login",
        " transport input all",
    ]

    return_value = task_9_3.clean_config(
        "config_r2_short.txt", ["ip", "service", "line"]
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_different_ignore_lines_2():
    """
    Перевірка роботи функції
    """
    correct_return_value = [
        "Current configuration : 4052 bytes",
        "version 15.2",
        "hostname PE_r2",
        " deny   10.0.0.0 0.0.255.255",
        " permit 10.0.0.0 0.255.255.255",
        "mpls ldp router-id Loopback0 force",
        "control-plane",
        " exec-timeout 0 0",
        " privilege level 15",
        " logging synchronous",
        " login",
        " transport input all",
    ]

    return_value = task_9_3.clean_config(
        "config_r2_short.txt", ["ip", "service", "line", "alias"]
    )
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
