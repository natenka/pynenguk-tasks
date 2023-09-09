import task_17_2
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, read_all_csv_content_as_list


def test_functions_created():
    """
    Перевірка, що функції створені
    """
    check_function_exists(task_17_2, "parse_sh_version")
    check_function_exists(task_17_2, "write_inventory_to_csv")


def test_parse_sh_version_return_value():
    """
    Перевірка роботи функції
    """
    with open("sh_version_r1.txt") as f:
        sh_version_r1 = f.read()
    with open("sh_version_r2.txt") as f:
        sh_version_r2 = f.read()

    correct_return_value_r1 = (
        "12.4(15)T1",
        "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
        "15 days, 8 hours, 32 minutes",
    )
    correct_return_value_r2 = (
        "12.4(4)T",
        "disk0:c7200-js-mz.124-4.T",
        "45 days, 8 hours, 22 minutes",
    )

    return_value_r1 = task_17_2.parse_sh_version(sh_version_r1)
    assert return_value_r1 != None, "Функція нічого не повертає"
    assert (
        type(return_value_r1) == tuple
    ), f"За завданням функція має повертати кортеж, а повертає {type(return_value_r1).__name__}"
    assert (
        correct_return_value_r1 == return_value_r1
    ), "Функція повертає неправильне значення для виводу r1"

    return_value_r2 = task_17_2.parse_sh_version(sh_version_r2)
    assert (
        correct_return_value_r2 == return_value_r2
    ), "Функція повертає неправильне значення для виводу r2"


def test_write_to_csv_return_value(tmpdir):
    """
    Перевірка роботи функції
    """
    correct_return_value = sorted(
        [
            ["hostname", "ios", "image", "uptime"],
            [
                "r1",
                "12.4(15)T1",
                "flash:c1841-advipservicesk9-mz.124-15.T1.bin",
                "15 days, 8 hours, 32 minutes",
            ],
            [
                "r2",
                "12.4(4)T",
                "disk0:c7200-js-mz.124-4.T",
                "45 days, 8 hours, 22 minutes",
            ],
            [
                "r3",
                "12.4(4)T",
                "disk0:c7200-js-mz.124-4.T",
                "5 days, 18 hours, 2 minutes",
            ],
        ]
    )
    sh_version_files = ["sh_version_r1.txt", "sh_version_r2.txt", "sh_version_r3.txt"]
    dest_filename = tmpdir.mkdir("test_tasks").join("routers_inventory.csv")
    return_value = task_17_2.write_inventory_to_csv(sh_version_files, dest_filename)
    csv_content = read_all_csv_content_as_list(dest_filename)

    assert (
        None == return_value
    ), f"За завданням функція має повертати None, а повертає {type(return_value).__name__}"
    assert correct_return_value == sorted(
        csv_content
    ), "Функція повертає неправильне значення"
