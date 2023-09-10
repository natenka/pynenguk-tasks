from importlib import reload
import sys
import pytest


def test_task_cfg_trunk_sw2(monkeypatch, tmpdir):
    """
    Перевірка роботи завдання на файле config_trunk_sw2.txt
    """
    monkeypatch.setattr("sys.argv", ["task_7_4.py", "config_trunk_sw2.txt"])
    import task_7_4

    correct_result = {
        "FastEthernet0/1": ["100", "200"],
        "FastEthernet0/3": ["100", "300", "400", "500", "600"],
        "FastEthernet0/4": ["400", "500", "600"],
    }

    task_vars = [var for var in dir(task_7_4) if not var.startswith("_")]

    assert "trunk_dict" in task_vars, "Словник має бути записаний у змінну trunk_dict"
    if not isinstance(task_7_4.trunk_dict, dict):
        pytest.fail(
            f"За завданням у змінній trunk_dict має бути словник, а в ній {type(task_7_4.result).__name__}"
        )
    assert (
        correct_result == task_7_4.trunk_dict
    ), f"У змінній trunk_dict має бути словник {correct_result}"


def test_task_cfg_trunk_sw3(monkeypatch, tmpdir):
    """
    Перевірка роботи завдання на файле config_trunk_sw3.txt
    """
    monkeypatch.setattr("sys.argv", ["task_7_4.py", "config_trunk_sw3.txt"])
    if sys.modules.get("task_7_4"):
        reload(sys.modules["task_7_4"])
    import task_7_4

    correct_result = {
        "FastEthernet0/1": ["10", "20", "21", "22"],
        "FastEthernet0/2": ["10", "13", "1450", "1451", "1452"],
        "FastEthernet0/6": ["40", "50", "60"],
    }

    task_vars = [var for var in dir(task_7_4) if not var.startswith("_")]

    assert "trunk_dict" in task_vars, "Словник має бути записаний у змінну trunk_dict"
    if not isinstance(task_7_4.trunk_dict, dict):
        pytest.fail(
            f"За завданням у змінній trunk_dict має бути словник, а в ній {type(task_7_4.result).__name__}"
        )
    assert (
        correct_result == task_7_4.trunk_dict
    ), f"У змінній trunk_dict має бути словник {correct_result}"
