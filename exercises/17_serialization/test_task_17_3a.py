import os
import yaml
import pytest
import task_17_3a
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    check_function_params,
    get_func_params_default_value,
)


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_17_3a, "generate_topology_from_cdp")


def test_function_params():
    check_function_params(
        function=task_17_3a.generate_topology_from_cdp,
        param_count=2,
        param_names=["list_of_files", "save_to_filename"],
    )
    default_values = get_func_params_default_value(
        task_17_3a.generate_topology_from_cdp
    )
    assert (
        default_values.get("save_to_filename") == None
    ), "У параметру save_to_filename значення за замовчанням має бути None"


def test_function_return_value():
    """
    Перевірка роботи функції
    """
    list_of_cdp_files = [
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r5.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r3.txt",
        "sh_cdp_n_r4.txt",
        "sh_cdp_n_r6.txt",
    ]
    correct_return_value = {
        "R2": {
            "Eth 0/0": {"SW1": "Eth 0/2"},
            "Eth 0/1": {"R5": "Eth 0/0"},
            "Eth 0/2": {"R6": "Eth 0/1"},
        },
        "R5": {"Eth 0/0": {"R2": "Eth 0/1"}, "Eth 0/1": {"R4": "Eth 0/1"}},
        "R1": {"Eth 0/0": {"SW1": "Eth 0/1"}},
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        },
        "R3": {"Eth 0/0": {"SW1": "Eth 0/3"}},
        "R4": {"Eth 0/0": {"SW1": "Eth 0/4"}, "Eth 0/1": {"R5": "Eth 0/1"}},
        "R6": {"Eth 0/1": {"R2": "Eth 0/2"}},
    }

    return_value = task_17_3a.generate_topology_from_cdp(list_of_cdp_files)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, dict):
        pytest.fail(
            f"За завданням функція має повертати словник, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_writing_to_yaml_file(tmpdir):
    list_of_cdp_files = [
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r5.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r3.txt",
        "sh_cdp_n_r4.txt",
        "sh_cdp_n_r6.txt",
    ]
    correct_return_value = {
        "R2": {
            "Eth 0/0": {"SW1": "Eth 0/2"},
            "Eth 0/1": {"R5": "Eth 0/0"},
            "Eth 0/2": {"R6": "Eth 0/1"},
        },
        "R5": {"Eth 0/0": {"R2": "Eth 0/1"}, "Eth 0/1": {"R4": "Eth 0/1"}},
        "R1": {"Eth 0/0": {"SW1": "Eth 0/1"}},
        "SW1": {
            "Eth 0/1": {"R1": "Eth 0/0"},
            "Eth 0/2": {"R2": "Eth 0/0"},
            "Eth 0/3": {"R3": "Eth 0/0"},
            "Eth 0/4": {"R4": "Eth 0/0"},
        },
        "R3": {"Eth 0/0": {"SW1": "Eth 0/3"}},
        "R4": {"Eth 0/0": {"SW1": "Eth 0/4"}, "Eth 0/1": {"R5": "Eth 0/1"}},
        "R6": {"Eth 0/1": {"R2": "Eth 0/2"}},
    }
    dest_filename = tmpdir.mkdir("test_tasks").join("topology.yaml")
    return_value = task_17_3a.generate_topology_from_cdp(
        list_of_cdp_files, save_to_filename=dest_filename
    )
    assert os.path.exists(dest_filename), "YAML файл не створено"
    with open(dest_filename) as f:
        yaml_file_content = yaml.safe_load(f)
    assert (
        correct_return_value == yaml_file_content
    ), "Топологія не записана в YAML файл"
