def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_6_2

    out, err = capsys.readouterr()
    correct_stdout = (
        "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"
    )
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"


def test_task_variables():
    """
    Проверка что в задании создана нужная переменная
    и в ней содержится правильный результат
    """
    import task_6_2

    # переменные созданные в задании:
    task_vars = [var for var in dir(task_6_2) if not var.startswith("_")]

    correct_result = "GUIdO vAn ROssUm bEgAn wOrkIng On PYthOn In thE lAtE 1980s"

    assert (
        "result" in task_vars
    ), "Итоговая строка должна быть записана в переменную result"
    assert (
        type(task_6_2.result) == str
    ), f"За завданням у змінній result має бути рядок, а ній {type(task_6_2.result).__name__}"
    assert (
        correct_result == task_6_2.result
    ), f"В переменной result должна быть строка '{correct_result}'"

