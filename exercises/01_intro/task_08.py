"""
Якщо запустити код завдання, на екран буде виведено:
$ python task_08.py
.py
.pyi
.pyc
.pyd
.pyw
.pyz

Надо изменить код так, чтобы при запуске кода был такой вывод
$ python task_08.py
script.py
script.pyi
script.pyc
script.pyd
script.pyw
script.pyz

При этом добавление слова script должно выполняться именно через переменную
filename и нельзя менять список python_extensions.
"""
filename = "script"
python_extensions = ['.py', '.pyi', '.pyc', '.pyd', '.pyw', '.pyz']
for ext in python_extensions:
    print(ext)

