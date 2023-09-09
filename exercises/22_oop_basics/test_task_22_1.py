import task_22_1
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    unify_topology_dict,
)


def test_class_created():
    check_class_exists(task_22_1, "Topology")


def test_attr_topology(topology_with_dupl_links):
    return_value = task_22_1.Topology(topology_with_dupl_links)
    check_attr_or_method(return_value, attr="topology")


def test_topology_normalization():
    topology_with_dupl_links = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    correct_topology = unify_topology_dict(
        {
            ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
            ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
            ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
            ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
            ("R3", "Eth0/1"): ("R4", "Eth0/0"),
            ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        }
    )

    return_value = task_22_1.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"За завданням у змінній topology должен быть словарь, а не {type(return_value.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"
    assert (
        correct_topology == return_topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"
