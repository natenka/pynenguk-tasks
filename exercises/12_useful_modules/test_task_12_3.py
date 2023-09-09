import task_12_3
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_function_exists,
    unified_columns_output,
)


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_12_3, "print_ip_table")


def test_function_stdout(capsys):
    """
    Перевірка роботи завдання
    """
    reach_ip = ["10.10.1.7", "10.10.1.8", "10.10.1.9", "10.10.1.15"]
    unreach_ip = ["10.10.2.1", "10.10.1.2"]
    return_value = task_12_3.print_ip_table(reach_ip, unreach_ip)

    stdout, err = capsys.readouterr()
    correct_stdout = unified_columns_output(
        "Reachable    Unreachable\n"
        "-----------  -------------\n"
        "10.10.1.7    10.10.2.1\n"
        "10.10.1.8    10.10.1.2\n"
        "10.10.1.9\n"
        "10.10.1.15\n"
    )
    assert return_value == None, "Функція повинна повертати None"
    assert correct_stdout == unified_columns_output(
        stdout
    ), "Функція повертає неправильне значення"
