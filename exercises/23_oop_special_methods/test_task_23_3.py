import task_23_3
import sys

sys.path.append("..")

from pyneng_common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    check_class_exists(task_23_3, "Topology")


def test_attr_topology(topology_with_dupl_links):
    top_with_data = task_23_3.Topology(topology_with_dupl_links)
    check_attr_or_method(top_with_data, attr="topology")


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    top_with_data = task_23_3.Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method__add__(normalized_topology_example):
    top1 = task_23_3.Topology(normalized_topology_example)
    top1_size_before_add = len(top1.topology)
    top2 = task_23_3.Topology(
        {("R1", "Eth0/4"): ("R7", "Eth0/0"), ("R1", "Eth0/6"): ("R9", "Eth0/0")}
    )
    top2_size_before_add = len(top2.topology)

    check_attr_or_method(top1, method="__add__")
    top3 = top1 + top2
    assert isinstance(
        top3, task_23_3.Topology
    ), "Метод __add__ має повернути новий екземпляр класу Topology"
    assert len(top3.topology) == 8
    assert (
        len(top1.topology) == top1_size_before_add
    ), "Після додавання змінився розмір першої топології. Метод __add__ не повинен змінювати вихідні топології"
    assert (
        len(top2.topology) == top2_size_before_add
    ), "Після додавання змінився розмір першої топології. Метод __add__ не повинен змінювати вихідні топології"
