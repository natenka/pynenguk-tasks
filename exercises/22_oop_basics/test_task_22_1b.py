import task_22_1b
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    unify_topology_dict,
)


def test_class_created():
    check_class_exists(task_22_1b, "Topology")


def test_attr_topology(topology_with_dupl_links):
    top_with_data = task_22_1b.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1b.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"За завданням у змінній topology повинен бути словник, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"


def test_method_delete_link_created(
    topology_with_dupl_links, normalized_topology_example
):
    norm_top = task_22_1b.Topology(normalized_topology_example)
    check_attr_or_method(norm_top, method="delete_link")


def test_method_delete_link(normalized_topology_example, capsys):
    norm_top = task_22_1b.Topology(normalized_topology_example)
    delete_link_result = norm_top.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    assert None == delete_link_result, "Метод delete_link не повинен нічого повертати"

    assert ("R3", "Eth0/0") not in norm_top.topology, "З'єднання не видалено"

    norm_top.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    assert ("R3", "Eth0/2") not in norm_top.topology, "З'єднання не видалено"

    norm_top.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))
    out, err = capsys.readouterr()
    link_msg = "There is no such link"
    assert (
        link_msg in out
    ), "При видаленні неіснуючого з'єднання не було виведено повідомлення ''There is no such link'"
