import pytest

try:
    import task_11_1a
except OSError:
    pytest.fail(
        "Для цього завдання функцію треба ОБОВ'ЯЗКОВО викликати у блоці if __name__ == '__main__':"
    )

import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_11_1a, "convert_mac_list")


@pytest.mark.parametrize(
    "mac_list,correct_converted_mac_list",
    [
        (
            ["1a1b.2c2d.3e3f", "aaaabbbbcccc"],
            ["1a:1b:2c:2d:3e:3f", "aa:aa:bb:bb:cc:cc"],
        ),
        (
            ["1111:2222:3333", "1a-1b-2c-2d-3e-3f"],
            ["11:11:22:22:33:33", "1a:1b:2c:2d:3e:3f"],
        ),
    ],
)
def test_function_return_value_correct_mac(mac_list, correct_converted_mac_list):
    """
    Перевірка роботи функції
    """

    return_value = task_11_1a.convert_mac_list(mac_list)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, list):
        pytest.fail(
            f"За завданням функція має повертати список, а повертає {type(return_value).__name__}"
        )
    assert correct_converted_mac_list == return_value, (
        f"Функція повертає неправильне значення.\nЯкщо функції передається "
        f"як аргумент список {mac_list},\nрезультат має бути {correct_converted_mac_list}"
    )


@pytest.mark.parametrize(
    "wrong_mac_list",
    [
        ["1a.2c2d.3e3f", "1a1b.2c2d.3e3f"],
        ["1111:2222:3333", "aaaabbRRcccc"],
        ["1111:2222:333333", "11:11:22:22:33:33"],
        ["1a-1b-2c-2d-3e-3f-aa"],
    ],
)
def test_function_return_value_wrong_mac_strict_true(wrong_mac_list):
    """
    Перевірка роботи функції с неправильними MAC-адресами
    """
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_1a.convert_mac_list(wrong_mac_list, strict=True)


@pytest.mark.parametrize(
    "mac_list,correct_converted_mac_list",
    [
        (
            ["1a1b.WWWW.3e3f", "aaaabbbbcccc"],
            ["aa:aa:bb:bb:cc:cc"],
        ),
        (
            ["1111:2222:33", "1a-1b-2c-2d-3e-3f"],
            ["1a:1b:2c:2d:3e:3f"],
        ),
    ],
)
def test_function_return_value_wrong_mac_strict_false(
    mac_list, correct_converted_mac_list
):
    """
    Перевірка роботи функції
    """
    return_value = task_11_1a.convert_mac_list(mac_list, strict=False)
    assert correct_converted_mac_list == return_value, (
        f"Функція повертає неправильне значення.\nЯкщо функції передається "
        f"як аргумент список {mac_list},\nрезультат має бути {correct_converted_mac_list}"
    )
