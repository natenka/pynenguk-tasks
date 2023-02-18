import pytest
import task_24_2a
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_24_2a, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_2a.MyNetmiko(**first_router_from_devices_yaml)
    ssh.disconnect()
    assert isinstance(
        ssh, CiscoIosSSH
    ), "Клас MyNetmiko має успадкувати від CiscoIosSSH"
    check_attr_or_method(ssh, method="send_command")
    check_attr_or_method(ssh, method="_check_error_in_command")


@pytest.mark.parametrize(
    "error,command",
    [
        ("Invalid input detected", "sh ip br"),
        ("Incomplete command", "copy"),
        ("Ambiguous command", "a"),
    ],
)
def test_errors(first_router_from_devices_yaml, command, error):
    ssh = task_24_2a.MyNetmiko(**first_router_from_devices_yaml)
    output = ssh.send_command("sh run | i hostname")
    assert (
        "hostname" in output
    ), "При створенні екземпляра класу має створюватися підключення та перехід у режим enable"

    with pytest.raises(task_24_2a.ErrorInCommand) as excinfo:
        return_value = ssh.send_command(command)
    ssh.disconnect()
    assert error in str(
        excinfo
    ), "Метод send_command повинен генерувати виключення, коли команда виконана з помилкою"
