def test_task(capsys):
    """
    Перевірка роботи завдання при вводе access
    """
    import task_6_7

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface FastEthernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,20,30,40\n"
        "interface FastEthernet0/2\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 11,30\n"
        "interface FastEthernet0/4\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan remove 17\n"
        "interface FastEthernet0/5\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan add 10,21\n"
        "interface FastEthernet0/7\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport mode trunk\n"
        " switchport trunk allowed vlan 30"
    )

    assert out, (
        "Нічого не виведено стандартний потік виведення. Потрібно не лише "
        "отримати потрібний результат, але й вивести його на стандартний потік "
        "виведення за допомогою print"
    )
    assert (
        correct_stdout == out.strip()
    ), "На стандартний потік виведення виводиться неправильний вивід"
