import pytest

try:
    import task_18_2c
except OSError:
    pytest.fail(
        "Для цього завдання функцію треба ОБОВ'ЯЗКОВО викликати у блоці if __name__ == '__main__':"
    )

import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


correct_return_value = (
    {
        "ip http server": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#ip http server\n"
        "R1(config)#",
        "logging buffered 20010": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging buffered 20010\n"
        "R1(config)#",
    },
    {
        "a": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#a\n"
        '% Ambiguous command:  "a"\n'
        "R1(config)#",
        "logging": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging\n"
        "% Incomplete command.\n"
        "\n"
        "R1(config)#",
        "logging 0255.255.1": "config term\n"
        "Enter configuration commands, one per line.  End with CNTL/Z.\n"
        "R1(config)#logging 0255.255.1\n"
        "                   ^\n"
        "% Invalid input detected at '^' marker.\n"
        "\n"
        "R1(config)#",
    },
)

commands_with_errors = ["logging 0255.255.1", "logging", "a"]
correct_commands = ["logging buffered 20010", "ip http server"]
test_commands = commands_with_errors + correct_commands


def test_functions_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_18_2c, "send_config_commands")


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_function_stdout(
    error, command, first_router_from_devices_yaml, capsys, monkeypatch
):
    monkeypatch.setattr("builtins.input", lambda x=None: "y")

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, [command], log=False
    )

    stdout, err = capsys.readouterr()
    ip = first_router_from_devices_yaml["host"]
    assert error in stdout, "У повідомленні про помилку немає самої помилки"
    assert command in stdout, "У повідомленні про помилку немає команди"
    assert ip in stdout, "У повідомленні про помилку немає IP-адреси прострою"


def test_function_return_value_continue_yes(
    first_router_from_devices_yaml, capsys, monkeypatch
):
    monkeypatch.setattr("builtins.input", lambda x=None: "y")

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, test_commands, log=False
    )

    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    assert type(return_value) == tuple, "Функція має повертати кортеж"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функція має повертати кортеж із двома словниками"
    correct_good, correct_bad = correct_return_value
    return_good, return_bad = return_value
    assert (
        correct_good.keys() == return_good.keys()
    ), "Функція повертає неправильне значення для словника з командами без помилок"
    assert (
        correct_bad.keys() == return_bad.keys()
    ), "Функція повертає неправильне значення для словника з командами з помилками"


@pytest.mark.parametrize(
    "c_map,commands_1,commands_2",
    [
        (("good", "bad"), correct_commands[:2], commands_with_errors[:2]),
        (("bad", "good"), commands_with_errors[:1], correct_commands),
        (("good", "bad"), correct_commands[:1], commands_with_errors[1:2]),
    ],
)
def test_function_return_value_continue_no(
    first_router_from_devices_yaml, capsys, monkeypatch, c_map, commands_1, commands_2
):
    monkeypatch.setattr("builtins.input", lambda x=None: "n")
    commands = commands_1 + commands_2

    return_value = task_18_2c.send_config_commands(
        first_router_from_devices_yaml, commands, log=False
    )

    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    assert type(return_value) == tuple, "Функція має повертати кортеж"
    assert 2 == len(return_value) and all(
        type(item) == dict for item in return_value
    ), "Функція має повертати кортеж із двома словниками"
    return_good, return_bad = return_value
    if c_map[0] == "bad":
        commands_with_errors, correct_commands = commands_1, commands_2
        assert [] == list(return_good) and commands_with_errors[:1] == sorted(
            return_bad
        ), "Функція повертає неправильне значення"
    else:
        commands_with_errors, correct_commands = commands_2, commands_1
        assert correct_commands == list(return_good) and commands_with_errors[
            :1
        ] == list(return_bad), "Функція повертає неправильне значення"
