import task_18_2a
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, strip_empty_lines


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_2a, "send_config_commands")


def test_function_return_value(
    capsys, r1_test_connection, first_router_from_devices_yaml
):
    """
    Перевірка роботи функції
    """
    test_commands = [
        "interface Loopback 100",
        "ip address 10.1.1.100 255.255.255.255",
    ]
    correct_return_value = r1_test_connection.send_config_set(test_commands)
    return_value = task_18_2a.send_config_commands(
        first_router_from_devices_yaml, test_commands
    )
    # проверяем возвращаемое значение
    assert return_value != None, "Функція нічого не повертає"
    assert (
        type(return_value) == str
    ), f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
    assert strip_empty_lines(return_value) == strip_empty_lines(
        correct_return_value
    ), "Функція повертає неправильне значення"

    # по умолчанию, log должно быть равным True
    # и на stdout должно выводиться сообщение
    correct_stdout = f"подключаюсь к {r1_test_connection.host}"
    stdout, err = capsys.readouterr()
    assert stdout != "", "Повідомлення про помилку не виведено на stdout"
    assert correct_stdout in stdout.lower(), "Виведено неправильне повідомлення про помилку"

    # проверяем, что с log=False вывода в stdout нет
    return_value = task_18_2a.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )
    correct_stdout = ""
    stdout, err = capsys.readouterr()
    assert (
        correct_stdout == stdout
    ), "Сообщение об ошибке не должно выводиться на stdout, когда log=False"
