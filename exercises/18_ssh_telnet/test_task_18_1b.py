import task_18_1b
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_1b, "send_show_command")


def test_function_return_value(capsys, first_router_wrong_ip):
    """
    Перевірка роботи функції
    """
    return_value = task_18_1b.send_show_command(first_router_wrong_ip, "sh ip int br")
    correct_stdout1 = "Connection to device timed-out"
    correct_stdout2 = "connection to device failed"
    out, err = capsys.readouterr()
    assert out != "", "Повідомлення про помилку не виведено на stdout"
    assert (
        correct_stdout1 in out or correct_stdout2 in out
    ), "Виведено неправильне повідомлення про помилку"
