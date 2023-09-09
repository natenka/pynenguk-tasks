import pytest
import task_22_2c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
)


def test_class_created():
    check_class_exists(task_22_2c, "CiscoTelnet")


def test_send_config_commands_correct_commands(first_router_from_devices_yaml, capsys):
    r1 = task_22_2c.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_config_commands")

    correct_commands = ["interface loop55", "ip address 5.5.5.5 255.255.255.255"]
    return_value = r1.send_config_commands(correct_commands)
    assert (
        correct_commands[0] in return_value and correct_commands[1] in return_value
    ), "Метод send_config_commands повертає неправильне значення"


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "logging 0255.255.1"),
        ("Incomplete command", "logging"),
        ("Ambiguous command", "a"),
    ],
)
def test_send_config_commands_wrong_commands(
    first_router_from_devices_yaml, capsys, error, command
):
    r1 = task_22_2c.CiscoTelnet(**first_router_from_devices_yaml)

    return_value = r1.send_config_commands(command, strict=False)
    stdout, err = capsys.readouterr()
    assert (
        error in stdout
    ), "Метод send_config_commands не виводить повідомлення про помилку"

    with pytest.raises(ValueError) as excinfo:
        return_value = r1.send_config_commands(command, strict=True)
    assert error in str(
        excinfo
    ), "Метод send_config_commands має генерувати виняток, коли strict=True"
