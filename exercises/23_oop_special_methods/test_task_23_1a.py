import task_23_1a
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_23_1a, "IPAddress")


def test_attr_topology():
    return_ip = task_23_1a.IPAddress("10.1.1.1/24")
    check_attr_or_method(return_ip, attr="ip")
    check_attr_or_method(return_ip, attr="mask")
    assert "10.1.1.1" == return_ip.ip, "Значення return_ip.ip має дорівнювати 10.1.1.1"
    assert 24 == return_ip.mask, "Значення return_ip.mask має дорівнювати 24"


def test_str_method():
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert (
        str(return_ip) == "IP address 10.5.5.5/24"
    ), "Метод __str__ повинен повертати 'IP address 10.5.5.5/24'"


def test_repr_method():
    return_ip = task_23_1a.IPAddress("10.5.5.5/24")
    assert (
        repr(return_ip).replace('"', "'") == "IPAddress('10.5.5.5/24')"
    ), "Метод __repr__ повинен повертати IPAddress('10.5.5.5/24')"
