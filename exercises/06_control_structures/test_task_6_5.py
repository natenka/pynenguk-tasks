import pytest
from importlib import reload
import re
import sys

sys.path.append("..")

from pyneng_common_functions import count_calls


@count_calls
def monkey_input_number_5(prompt):
    __tracebackhide__ = True
    if monkey_input_number_5.total_calls == 1:
        return "3"
    elif monkey_input_number_5.total_calls == 2:
        return "8"
    elif monkey_input_number_5.total_calls == 3:
        return "5"
    else:
        pytest.fail(
            "Запит чисел у користувача повинен зупинитися після того, як було"
            "введено вірне число"
        )


@count_calls
def monkey_input_number_8(prompt):
    __tracebackhide__ = True
    if monkey_input_number_8.total_calls == 1:
        return "7"
    elif monkey_input_number_8.total_calls == 2:
        return "8"
    else:
        pytest.fail(
            "Запит чисел у користувача повинен зупинитися після того, як було"
            "введено вірне число"
        )


def test_task_random_5_input_3_8_5(capsys, monkeypatch):
    """
    Перевірка роботи завдання при задуманном числе 5 и вводе 3, 8, 5
    """
    monkeypatch.setattr("random.randint", lambda x, y: 5)
    monkeypatch.setattr("builtins.input", monkey_input_number_5)
    import task_6_5

    correct_stdout = (
        "\nEnter number: 3\n"
        "Your guess is too low\n"
        "Enter number: 8\n"
        "Your guess is too high\n"
        "Enter number: 5\n"
        "Correct!\n"
    )
    out, err = capsys.readouterr()
    out = out.strip().lower()
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert "high" in out and "low" in out and "correct" in out, (
        f"При задуманому числі 5 та введення користувача 3, 8, 5, на стандартному "
        f"потоці виводу повинен бути такий вивід {correct_stdout}"
    )


def test_task_random_8_input_7_8(capsys, monkeypatch):
    """
    Перевірка роботи завдання при задуманном числе 8 и вводе 7, 8
    """
    monkeypatch.setattr("random.randint", lambda x, y: 8)
    monkeypatch.setattr("builtins.input", monkey_input_number_8)
    if sys.modules.get("task_6_5"):
        reload(sys.modules["task_6_5"])
    import task_6_5

    correct_stdout = (
        "\nEnter number: 7\n" "Your guess is too low\n" "Enter number: 8\n" "Correct!\n"
    )
    out, err = capsys.readouterr()
    out = out.strip().lower()
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert "low" in out and "correct" in out, (
        f"При задуманому числі 8 та введення користувача 7, 8 на стандартному "
        f"потоці виводу повинен бути такий вивід {correct_stdout}"
    )


def test_task_random_4_input_1_1_1_1_1(capsys, monkeypatch):
    """
    Перевірка роботи завдання при задуманном числе 4 и вводе 1, 1, 1, 1, 1
    """
    monkeypatch.setattr("random.randint", lambda x, y: 4)
    monkeypatch.setattr("builtins.input", lambda x: "1")
    if sys.modules.get("task_6_5"):
        reload(sys.modules["task_6_5"])
    import task_6_5

    correct_stdout = (
        "\nEnter number: 1\n"
        "Your guess is too low\n"
        "\nEnter number: 1\n"
        "Your guess is too low\n"
        "\nEnter number: 1\n"
        "Your guess is too low\n"
        "\nEnter number: 1\n"
        "Your guess is too low\n"
        "\nEnter number: 1\n"
        "Your guess is too low\n"
        "Number not guessed after 5 tries\n"
    )
    out, err = capsys.readouterr()
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert 5 == out.lower().count("low") and "not guessed" in out.lower(), (
        f"При задуманому числі 8 та введення користувача 1, 1, 1, 1, 1 на стандартному "
        f"потоці виводу повинен бути такий вивід {correct_stdout}"
    )
