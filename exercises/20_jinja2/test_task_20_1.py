import task_20_1
import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines


def test_functions_created():
    check_function_exists(task_20_1, "generate_config")


def test_function_return_value():
    correct_return_value = (
        "\n"
        "hostname R3\n"
        "\n"
        "interface Loopback0\n"
        " ip address 10.0.0.3 255.255.255.255\n"
        "\n"
        "vlan 10\n"
        " name Marketing\n"
        "vlan 20\n"
        " name Voice\n"
        "vlan 30\n"
        " name Management\n"
        "\n"
        "router ospf 1\n"
        " router-id 10.0.0.3\n"
        " auto-cost reference-bandwidth 10000\n"
        " network 10.0.1.0 0.0.0.255 area 0\n"
        " network 10.0.2.0 0.0.0.255 area 2\n"
        " network 10.1.1.0 0.0.0.255 area 0\n"
    )

    template = "templates/for.txt"
    data = {
        "id": 3,
        "name": "R3",
        "vlans": {10: "Marketing", 20: "Voice", 30: "Management"},
        "ospf": [
            {"network": "10.0.1.0 0.0.0.255", "area": 0},
            {"network": "10.0.2.0 0.0.0.255", "area": 2},
            {"network": "10.1.1.0 0.0.0.255", "area": 0},
        ],
    }
    return_value = task_20_1.generate_config(template, data)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, str):
        pytest.fail(
            f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
        )
    assert strip_empty_lines(correct_return_value) == strip_empty_lines(
        return_value
    ), "Функція повертає неправильне значення"
