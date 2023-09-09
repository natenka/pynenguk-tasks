import task_22_1d
import sys

sys.path.append("..")

from pyneng_common_functions import (
    check_class_exists,
    check_attr_or_method,
    unify_topology_dict,
)


def test_class_created():
    check_class_exists(task_22_1d, "Topology")


def test_attr_topology(topology_with_dupl_links):
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    check_attr_or_method(return_value, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    correct_topology = unify_topology_dict(normalized_topology_example)
    return_value = task_22_1d.Topology(topology_with_dupl_links)
    assert (
        type(return_value.topology) == dict
    ), f"За завданням у змінній topology має бути словник, а не {type(return_value.topology).__name__}"
    assert len(correct_topology) == len(
        return_value.topology
    ), "Після створення екземпляра, у змінній topology повинна бути топологія без дублів"


def test_method_add_link_created(normalized_topology_example):
    return_value = task_22_1d.Topology(normalized_topology_example)
    check_attr_or_method(return_value, method="add_link")


def test_method_add_link(normalized_topology_example, capsys):
    return_value = task_22_1d.Topology(normalized_topology_example)

    add_link_result = return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    assert None == add_link_result, "Метод add_link не повинен нічого повертати"

    assert (
        "R1",
        "Eth0/4",
    ) in return_value.topology, (
        "Після додавання з'єднання через метод add_link воно має існувати в топології"
    )
    assert 7 == len(
        return_value.topology
    ), "Після додавання з'єднання кількість з'єднань повинна дорівнювати 7"

    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/0"))
    out, err = capsys.readouterr()
    assert (
        "Such a link already exists" in out
    ), "При додаванні існуючого з'єднання не було виведено повідомлення 'Such a link already exists'"

    return_value.add_link(("R1", "Eth0/4"), ("R7", "Eth0/5"))
    out, err = capsys.readouterr()
    assert (
        "A link to one of the ports exists" in out
    ), "При додаванні з'єднання з існуючим портом не було виведено повідомлення ''A link to one of the ports exists'"
