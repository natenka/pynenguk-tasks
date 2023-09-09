from importlib import reload
import sys

sys.path.append("..")

from pyneng_common_functions import count_calls


@count_calls
def monkey_input_access(prompt):
    __tracebackhide__ = True
    if monkey_input_access.total_calls == 1:
        return "access"
    elif monkey_input_access.total_calls == 2:
        return "Gi0/3"
    elif monkey_input_access.total_calls == 3:
        return "55"


@count_calls
def monkey_input_trunk(prompt):
    __tracebackhide__ = True
    if monkey_input_trunk.total_calls == 1:
        return "trunk"
    elif monkey_input_trunk.total_calls == 2:
        return "Gi0/2"
    elif monkey_input_trunk.total_calls == 3:
        return "10,11,12"


def test_task_access(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні access
    """
    monkeypatch.setattr("builtins.input", monkey_input_access)
    import task_5_5

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/3\n"
        "switchport mode access\n"
        "switchport access vlan 55\n"
        "switchport nonegotiate\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable"
    )

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"


def test_task_trunk(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні trunk
    """
    monkeypatch.setattr("builtins.input", monkey_input_trunk)
    if sys.modules.get("task_5_5"):
        reload(sys.modules["task_5_5"])
    import task_5_5

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/2\n"
        "switchport trunk encapsulation dot1q\n"
        "switchport mode trunk\n"
        "switchport trunk allowed vlan 10,11,12"
    )
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
