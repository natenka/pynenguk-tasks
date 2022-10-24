from importlib import reload
import sys


def test_task_r2(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні r2
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "r2")
    import task_5_3

    out, err = capsys.readouterr()
    r2_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    }

    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        str(r2_dict) in out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"


def test_task_sw1(capsys, monkeypatch):
    """
    Перевірка роботи завдання при введенні sw1
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "sw1")
    if sys.modules.get("task_5_3"):
        reload(sys.modules["task_5_3"])
    import task_5_3

    out, err = capsys.readouterr()
    sw1_dict = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
    assert (
        out
    ), "Нічого не виведено стандартний потік виведення. Потрібно не лише отримати потрібний результат, але й вивести його на стандартний потік виведення за допомогою print"
    assert (
        str(sw1_dict) in out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
