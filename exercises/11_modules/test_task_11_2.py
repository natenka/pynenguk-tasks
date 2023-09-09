import pytest

try:
    import task_11_2
except OSError:
    pytest.fail(
        "Для цього завдання функцію треба ОБОВ'ЯЗКОВО викликати у блоці if __name__ == '__main__':"
    )
import sys

sys.path.append("..")

from pyneng_common_functions import check_function_exists, count_calls


@count_calls
def monkey_input_retry_3(prompt):
    __tracebackhide__ = True
    if monkey_input_retry_3.total_calls == 1:
        return "10.a.1.1"
    elif monkey_input_retry_3.total_calls == 2:
        return "10.500.1.1"
    elif monkey_input_retry_3.total_calls == 3:
        return "a"
    else:
        pytest.fail("При max_retry=3 адреса повинна запитуватись лише три рази")


def test_function_created():
    """
    Тестуємо, що функцію створено
    """
    check_function_exists(task_11_2, "prompt_user_ip")


def test_function_return_value(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.1")
    correct_return_value = "10.1.1.1"
    return_value = task_11_2.prompt_user_ip(max_retry=5, ensure_unicast=False)
    if return_value is None:
        pytest.fail("Функція нічого не повертає")
    if not isinstance(return_value, str):
        pytest.fail(
            f"За завданням функція має повертати рядок, а повертає {type(return_value).__name__}"
        )
    assert correct_return_value == return_value, "Функція повертає неправильне значення"


def test_function_return_value_wrong_ip(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x=None: "500.1.1.1")
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_2.prompt_user_ip(max_retry=3, ensure_unicast=False)


def test_function_return_value_wrong_unicast_ip(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x=None: "224.1.1.1")
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_2.prompt_user_ip(max_retry=3, ensure_unicast=True)


def test_function_max_retry(monkeypatch):
    monkeypatch.setattr("builtins.input", monkey_input_retry_3)
    with pytest.raises(ValueError) as excinfo:
        return_value = task_11_2.prompt_user_ip(max_retry=3, ensure_unicast=False)
