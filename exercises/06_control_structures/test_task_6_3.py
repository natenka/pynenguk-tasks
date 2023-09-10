import pytest


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_6_3

    out, err = capsys.readouterr()
    correct_stdout = "[100, 30, 10, 20, 15, 100]"
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"


def test_task_variables():
    """
    Перевірка, що в завданні створена потрібна змінна
    і в ній міститься правильний результат
    """
    import task_6_3

    task_vars = [var for var in dir(task_6_3) if not var.startswith("_")]

    correct_result = [100, 30, 10, 20, 15, 100]

    assert "result" in task_vars, "Список має бути записаний у змінну result"
    if not isinstance(task_6_3.result, list):
        pytest.fail(
            f"За завданням у змінній result має бути список, а в ній {type(task_6_3.result).__name__}"
        )
    assert (
        correct_result == task_6_3.result
    ), f"У змінній result має бути список {correct_result}"
