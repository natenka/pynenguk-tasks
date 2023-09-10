import task_11_3
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, check_function_params


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_11_3, "parse_cdp_neighbors")


def test_function_params():
    """
    Перевірка імен та кількості параметрів
    """
    check_function_params(
        function=task_11_3.parse_cdp_neighbors,
        param_count=1,
        param_names=["command_output"],
    )


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    sh_cdp_n_sw1 = (
        "SW1>show cdp neighbors\n\n"
        "Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n"
        "                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone\n\n"
        "Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID\n"
        "R1           Eth 0/1         122           R S I           2811       Eth 0/0\n"
        "R2           Eth 0/2         143           R S I           2811       Eth 0/0\n"
        "R3           Eth 0/3         151           R S I           2811       Eth 0/0\n"
        "R6           Eth 0/5         121           R S I           2811       Eth 0/1"
    )
    correct_return_value = {
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
        ("SW1", "Eth0/5"): ("R6", "Eth0/1"),
    }

    return_value = task_11_3.parse_cdp_neighbors(sh_cdp_n_sw1)
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
    sh_cdp_n_r3 = (
        "R3>show cdp neighbors\n"
        "Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge\n"
        "                  S - Switch, H - Host, I - IGMP, r - Repeater\n\n"
        "Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID\n"
        "SW1              Eth 0/0            131          S I      WS-C3750- Eth 0/3\n"
        "R4               Eth 0/1            145        R S I      2811      Eth 0/0\n"
        "R5               Eth 0/2            123        R S I      2811      Eth 0/0\n"
    )
    correct_return_value = {
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }

    return_value = task_11_3.parse_cdp_neighbors(sh_cdp_n_r3)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"
