def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_9a

    out, err = capsys.readouterr()
    correct_stdout = "Guido Rossum working Python the 1980s"
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert correct_stdout == out.strip(), "На стандартний потік виведення виводиться неправильний рядок"
