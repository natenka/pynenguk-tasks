from importlib import reload
import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


def test_task_10_5_5_0_24(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні 10.5.5.0 255.255.255.0
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.0 255.255.255.0")
    import task_5_4a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert correct_stdout == stdout, "Виведено невірне значення"


def test_task_10_1_1_192_28(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні 10.1.1.192 255.255.255.240
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.192 255.255.255.240")
    if sys.modules.get("task_5_4a"):
        reload(sys.modules["task_5_4a"])
    import task_5_4a

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000\n\n"
        "Mask:\n"
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert correct_stdout == stdout, "Виведено невірне значення"
