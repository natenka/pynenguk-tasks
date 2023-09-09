import task_18_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_1a, "send_show_command")


def test_function_return_value(capsys, first_router_wrong_pass):
    """
    Перевірка роботи функції
    """
    return_value = task_18_1a.send_show_command(first_router_wrong_pass, "sh ip int br")
    correct_stdout = "authentication"
    out, err = capsys.readouterr()
    assert out != "", "Повідомлення про помилку не виведено на stdout"
    assert (
        correct_stdout in out.lower()
    ), "Виведено неправильне повідомлення про помилку"
