import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_4_6

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартний потік виведення виводиться неправильний рядок"
