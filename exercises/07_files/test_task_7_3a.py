import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


def test_task_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    import task_7_3a

    out, err = capsys.readouterr()
    out = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "10       01ab.c5d0.70d0      Gi0/8\n"
        "10       0a1b.1c80.7000      Gi0/4\n"
        "100      01bb.c580.7000      Gi0/1\n"
        "200      0a4b.c380.7c00      Gi0/2\n"
        "200      1a4b.c580.7000      Gi0/6\n"
        "300      0a1b.5c80.70f0      Gi0/7\n"
        "300      a2ab.c5a0.700e      Gi0/3\n"
        "500      02b1.3c80.7b00      Gi0/5\n"
        "1000     0a4b.c380.7d00      Gi0/9"
    )
    correct_stdout_lambda = unified_columns_output(
        "10        0a1b.1c80.7000      Gi0/4\n"
        "10        01ab.c5d0.70d0      Gi0/8\n"
        "100       01bb.c580.7000      Gi0/1\n"
        "200       0a4b.c380.7c00      Gi0/2\n"
        "200       1a4b.c580.7000      Gi0/6\n"
        "300       a2ab.c5a0.700e      Gi0/3\n"
        "300       0a1b.5c80.70f0      Gi0/7\n"
        "500       02b1.3c80.7b00      Gi0/5\n"
        "1000      0a4b.c380.7d00      Gi0/9\n"
    )
    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out or correct_stdout_lambda == out
    ), "На стандартний потік виведення виводиться неправильний рядок"
