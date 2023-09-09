from importlib import reload
import sys
import pytest


@pytest.mark.parametrize(
    "sep,correct_output",
    [
        ("|", "Guido|van|Rossum|began|working|on|Python"),
        ("===", "Guido===van===Rossum===began===working===on===Python"),
        ("__", "Guido__van__Rossum__began__working__on__Python"),
    ],
)
def test_task_sw1(capsys, monkeypatch, sep, correct_output):
    """
    Перевірка роботи завдання при введенні sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: sep)
    if sys.modules.get("task_5_2"):
        reload(sys.modules["task_5_2"])
    import task_5_2

    out, err = capsys.readouterr()
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_output == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
