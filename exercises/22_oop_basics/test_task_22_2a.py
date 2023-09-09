import os
import task_22_2a
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    strip_empty_lines,
)


def test_class_created():
    check_class_exists(task_22_2a, "CiscoTelnet")


def test_send_show_command_parse_true(
    first_router_from_devices_yaml, r1_test_telnet_connection
):
    full_pth = os.path.join(os.getcwd(), "templates")
    os.environ["NET_TEXTFSM"] = full_pth

    r1 = task_22_2a.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_show_command")

    correct_return_value = r1_test_telnet_connection.send_command(
        "sh ip int br", use_textfsm=True
    )
    return_value = r1.send_show_command(
        "sh ip int br", parse=True, templates="templates", index="index"
    )
    assert (
        correct_return_value == return_value
    ), "Метод send_show_command повертає неправильне значення з parse=True"


def test_send_show_command_parse_false(
    first_router_from_devices_yaml, r1_test_telnet_connection
):
    r1 = task_22_2a.CiscoTelnet(**first_router_from_devices_yaml)

    correct_return_value = r1_test_telnet_connection.send_command(
        "sh ip int br", strip_command=False, strip_prompt=False
    )
    return_value = r1.send_show_command(
        "sh ip int br", parse=False, templates="templates", index="index"
    )
    assert strip_empty_lines(correct_return_value) == strip_empty_lines(
        return_value
    ), "Метод send_show_command повертає неправильне значення з parse=False"


def test_send_show_command_different_command(
    first_router_from_devices_yaml, r1_test_telnet_connection
):
    full_pth = os.path.join(os.getcwd(), "templates")
    os.environ["NET_TEXTFSM"] = full_pth

    r1 = task_22_2a.CiscoTelnet(**first_router_from_devices_yaml)
    check_attr_or_method(r1, method="send_show_command")

    correct_return_value = r1_test_telnet_connection.send_command(
        "sh int desc", use_textfsm=True, strip_command=False, strip_prompt=False
    )
    return_value = r1.send_show_command(
        "sh int desc", parse=True, templates="templates", index="index"
    )
    assert (
        correct_return_value == return_value
    ), "Метод send_show_command повертає неправильне значення з parse=True"

    correct_return_value = r1_test_telnet_connection.send_command(
        "sh version | include IOS", strip_command=False, strip_prompt=False
    )
    return_value = r1.send_show_command(
        "sh version | include IOS", parse=False, templates="templates", index="index"
    )
    assert strip_empty_lines(correct_return_value) == strip_empty_lines(
        return_value
    ), "Метод send_show_command повертає неправильне значення з parse=False"
