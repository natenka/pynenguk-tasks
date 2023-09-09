import task_24_1
from base_connect_class import BaseSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_24_1, "CiscoSSH")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_1.CiscoSSH(**first_router_from_devices_yaml)
    assert isinstance(ssh, BaseSSH), "Клас CiscoSSH має успадкувати від BaseSSH"
    ssh.ssh.disconnect()
    check_attr_or_method(ssh, method="send_show_command")
    check_attr_or_method(ssh, method="send_cfg_commands")


def test_enable(first_router_from_devices_yaml):
    ssh = task_24_1.CiscoSSH(**first_router_from_devices_yaml)
    output = ssh.send_show_command("sh run | i hostname")
    ssh.ssh.disconnect()
    assert (
        "hostname" in output
    ), "При створенні екземпляра класу має створюватися підключення та перехід у режим enable"
