import pytest
import task_23_1
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_23_1, "IPAddress")


def test_attr_topology():
    return_ip = task_23_1.IPAddress("10.1.1.1/24")
    check_attr_or_method(return_ip, attr="ip")
    check_attr_or_method(return_ip, attr="mask")
    assert "10.1.1.1" == return_ip.ip, "Значення return_ip.ip має дорівнювати 10.1.1.1"
    assert 24 == return_ip.mask, "Значення return_ip.mask має дорівнювати 24"


def test_wrong_ip():
    with pytest.raises(ValueError) as excinfo:
        return_ip = task_23_1.IPAddress("10.1.1.1/240")
    with pytest.raises(ValueError) as excinfo:
        return_ip = task_23_1.IPAddress("10.1.400.1/24")
