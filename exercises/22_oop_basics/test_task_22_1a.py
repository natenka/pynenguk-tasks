import task_22_1a
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    unify_topology_dict,
)


def test_class_created():
    check_class_exists(task_22_1a, "Topology")


def test_attr_topology(topology_with_dupl_links):
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_method_normalize(topology_with_dupl_links):
    top_with_data = task_22_1a.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, method="_normalize")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1a.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"За завданням у змінній topology должен быть словарь, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"
    assert (
        correct_topology == return_topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"
