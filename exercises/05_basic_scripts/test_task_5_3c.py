import pytest
import sys

sys.path.append("..")

from pyneng_common_functions import count_calls


@count_calls
def monkey_input_r2(prompt):
    __tracebackhide__ = True
    if monkey_input_r2.total_calls == 1:
        return "r2"
    elif monkey_input_r2.total_calls == 2:
        return "ip"


@count_calls
def monkey_input_sw1(prompt):
    __tracebackhide__ = True
    if monkey_input_sw1.total_calls == 1:
        return "sw1"
    elif monkey_input_sw1.total_calls == 2:
        return "произвольная строка"


def test_task_r2_correct_param(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні r2
    """
    monkeypatch.setattr("builtins.input", monkey_input_r2)
    import task_5_3c

    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"


def test_task_sw1_wrong_param(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні sw1
    """
    monkeypatch.setattr("builtins.input", monkey_input_sw1)
    if sys.modules.get("task_5_3c"):
        del sys.modules["task_5_3c"]
    try:
        import task_5_3c
    except KeyError:
        pytest.fail(
            "У цьому завданні має бути оброблена ситуація, коли параметр"
            "вказаний неправильний. Не повинна виникати помилка KeyError"
        )

    out, err = capsys.readouterr()
    correct_stdout = "no such parameter"
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
