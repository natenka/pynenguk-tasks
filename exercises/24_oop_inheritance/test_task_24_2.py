import task_24_2
from netmiko.cisco.cisco_ios import CiscoIosSSH
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_24_2, "MyNetmiko")


def test_class_inheritance(first_router_from_devices_yaml):
    ssh = task_24_2.MyNetmiko(**first_router_from_devices_yaml)
    assert isinstance(
        ssh, CiscoIosSSH
    ), "Клас MyNetmiko має успадкувати від CiscoIosSSH"
    ssh.disconnect()
    check_attr_or_method(ssh, method="send_command")
    check_attr_or_method(ssh, method="send_config_set")


def test_enable(first_router_from_devices_yaml):
    ssh = task_24_2.MyNetmiko(**first_router_from_devices_yaml)
    output = ssh.send_command("sh run | i hostname")
    ssh.disconnect()
    assert (
        "hostname" in output
    ), "При створенні екземпляра класу має створюватися підключення та перехід у режим enable"
