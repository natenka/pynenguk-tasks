from pprint import pformat
from importlib import reload
import sys
import pytest


def test_task_cfg_trunk_sw2(monkeypatch, tmpdir):
    """
    Перевірка роботи завдання на файле config_trunk_sw2.txt
    """
    monkeypatch.setattr("sys.argv", ["task_7_5.py", "config_trunk_sw2.txt"])
    import task_7_5

    correct_result = {
        "FastEthernet0/1": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,200",
            "switchport mode trunk",
        ],
        "FastEthernet0/2": ["switchport mode access", "switchport access vlan 20"],
        "FastEthernet0/3": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 100,300,400,500,600",
            "switchport mode trunk",
        ],
        "FastEthernet0/4": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 400,500,600",
            "switchport mode trunk",
        ],
        "FastEthernet0/5": ["switchport mode access", "switchport access vlan 30"],
        "FastEthernet0/6": ["switchport mode access", "switchport access vlan 20"],
    }

    task_vars = [var for var in dir(task_7_5) if not var.startswith("_")]

    assert (
        "interface_dict" in task_vars
    ), "Словник має бути записаний у змінну interface_dict"
    if not isinstance(task_7_5.interface_dict, dict):
        pytest.fail(
            f"За завданням у змінній interface_dict має бути словник, а в ній {type(task_7_5.result).__name__}"
        )
    assert (
        correct_result == task_7_5.interface_dict
    ), f"У змінній interface_dict має бути словник \n{pformat(correct_result)}"


def test_task_cfg_trunk_sw3(monkeypatch, tmpdir):
    """
    Перевірка роботи завдання на файле config_trunk_sw3.txt
    """
    monkeypatch.setattr("sys.argv", ["task_7_5.py", "config_trunk_sw3.txt"])
    if sys.modules.get("task_7_5"):
        reload(sys.modules["task_7_5"])
    import task_7_5

    correct_result = {
        "FastEthernet0/1": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 10,20,21,22",
            "switchport mode trunk",
        ],
        "FastEthernet0/2": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 10,13,1450,1451,1452",
            "switchport mode trunk",
        ],
        "FastEthernet0/3": ["switchport mode access", "switchport access vlan 20"],
        "FastEthernet0/4": ["switchport mode access", "switchport access vlan 20"],
        "FastEthernet0/5": ["switchport mode access", "switchport access vlan 30"],
        "FastEthernet0/6": [
            "switchport trunk encapsulation dot1q",
            "switchport trunk allowed vlan 40,50,60",
            "switchport mode trunk",
        ],
        "FastEthernet0/7": ["switchport mode access"],
        "FastEthernet0/8": ["switchport mode access"],
    }

    task_vars = [var for var in dir(task_7_5) if not var.startswith("_")]

    assert (
        "interface_dict" in task_vars
    ), "Словник має бути записаний у змінну interface_dict"
    if not isinstance(task_7_5.interface_dict, dict):
        pytest.fail(
            f"За завданням у змінній interface_dict має бути словник, а в ній {type(task_7_5.result).__name__}"
        )
    assert (
        correct_result == task_7_5.interface_dict
    ), f"У змінній interface_dict має бути словник \n{pformat(correct_result)}"
