import sys

sys.path.append("..")

from pyneng_common_functions import unified_columns_output


def test_task(capsys):
    """
    Перевірка роботи завдання при вводе access
    """
    import task_7_1

    out, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Prefix                    10.0.24.0/24\n"
        "AD/Metric                 110/41\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d18h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.28.0/24\n"
        "AD/Metric                 110/31\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.37.0/24\n"
        "AD/Metric                 110/11\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.41.0/24\n"
        "AD/Metric                 110/51\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.78.0/24\n"
        "AD/Metric                 110/21\n"
        "Next-Hop                  10.0.13.3\n"
        "Last update               3d20h\n"
        "Outbound Interface        FastEthernet0/0\n"
        "Prefix                    10.0.79.0/24\n"
        "AD/Metric                 110/20\n"
        "Next-Hop                  10.0.19.9\n"
        "Last update               4d02h\n"
        "Outbound Interface        FastEthernet0/2\n"
    )

    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert correct_stdout == unified_columns_output(
        out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
