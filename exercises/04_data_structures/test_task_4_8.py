import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_8

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "192       168       3         1\n" "11000000  10101000  00000011  00000001\n"
    )
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"
