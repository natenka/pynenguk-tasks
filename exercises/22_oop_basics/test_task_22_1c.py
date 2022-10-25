import task_22_1c
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    unify_topology_dict,
)


def test_class_created():
    check_class_exists(task_22_1c, "Topology")


def test_attr_topology(topology_with_dupl_links):
    top_with_data = task_22_1c.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1c.Topology(topology_with_dupl_links)
    return_topology = unify_topology_dict(return_value.topology)
    assert (
        type(return_value.topology) == dict
    ), f"За завданням у змінній topology має бути словник, а не {type(top_with_data.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"


def test_method_delete_node_created(
    topology_with_dupl_links, normalized_topology_example
):
    return_value = task_22_1c.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="delete_node")


def test_method_delete_node(normalized_topology_example, capsys):
    return_value = task_22_1c.Topology(normalized_topology_example)

    node = "SW1"
    delete_node_result = return_value.delete_node(node)
    assert None == delete_node_result, "Метод delete_node не повинен нічого повертати"

    ports_with_node = [
        src for src, dst in return_value.topology.items() if node in src or node in dst
    ]
    assert 0 == len(ports_with_node), "З'єднання з хостом SW1 не видалено"
    assert 3 == len(
        return_value.topology
    ), "У топології повинні залишитися лише три з'єднання"

    return_value.delete_node(node)
    out, err = capsys.readouterr()
    assert (
        "There is no such device" in out
    ), "При видаленні неіснуючого пристрою не було виведено повідомлення 'There is no such device'"
