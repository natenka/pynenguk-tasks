import pytest


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_6_2

    out, err = capsys.readouterr()
    correct_stdout = "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"
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
    import task_6_2

    task_vars = [var for var in dir(task_6_2) if not var.startswith("_")]

    correct_result = "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"

    assert (
        "result" in task_vars
    ), "Підсумковий рядок повинен бути записаний у змінну result"
    if not isinstance(task_6_2.result, str):
        pytest.fail(
            f"За завданням у змінній result має бути рядок, а ній {type(task_6_2.result).__name__}"
        )
    assert (
        correct_result == task_6_2.result
    ), f"У змінній result має бути рядок '{correct_result}'"
