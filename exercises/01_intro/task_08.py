"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_08.py
.py
.pyi
.pyc
.pyd
.pyw
.pyz

Потрібно змінити код таким чином, щоб під час виконання коду був такий вивід
$ python task_08.py
script.py
script.pyi
script.pyc
script.pyd
script.pyw
script.pyz

При цьому додавання слова script має виконуватись саме через змінну filename і
не можна змінювати список python_extensions.
"""
filename = "script"
python_extensions = ['.py', '.pyi', '.pyc', '.pyd', '.pyw', '.pyz']
for ext in python_extensions:
    print(ext)

