def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_9b

    out, err = capsys.readouterr()
    correct_stdout = (
        "Guido\nvan\nRossum\nbegan\nworking\non\nPython\nin\nthe\nlate\n1980s"
    )
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"
