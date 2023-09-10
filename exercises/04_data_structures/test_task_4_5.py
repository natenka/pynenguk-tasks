import pytest


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_5

    out, err = capsys.readouterr()
    correct_stdout = "['1', '3', '8']"
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"


def test_task_variables():
    """
    Перевірка, що в завданні створена потрібна змінна
    і в ній міститься правильний результат
    """
    import task_4_5

    task_vars = [var for var in dir(task_4_5) if not var.startswith("_")]

    correct_result = ["1", "3", "8"]
    assert "result" in task_vars, "Список має бути записаний у змінну result"
    if not isinstance(task_4_5.result, list):
        pytest.fail(
            f"За завданням у змінній result має бути список, а в ній {type(task_4_5.result).__name__}"
        )
    assert (
        correct_result == task_4_5.result
    ), f"У змінній result має бути список {correct_result}"
