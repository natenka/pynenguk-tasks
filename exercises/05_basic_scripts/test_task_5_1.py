from importlib import reload
import sys
import pytest


@pytest.mark.parametrize(
    "index,correct_word", [("0", "guido"), ("5", "on"), ("6", "python")]
)
def test_task_sw1(capsys, monkeypatch, index, correct_word):
    """
    Перевірка роботи завдання при введенні sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: index)
    if sys.modules.get("task_5_1"):
        reload(sys.modules["task_5_1"])
    import task_5_1

    out, err = capsys.readouterr()
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_word in out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
