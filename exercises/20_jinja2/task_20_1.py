# -*- coding: utf-8 -*-
"""
Завдання 20.1

Створити функцію generate_config.

Параметри функції:
* template - шлях до файлу із шаблоном (наприклад, "templates/for.txt")
* data_dict - словник із значеннями, які треба підставити у шаблон

Функція повинна повертати рядок зі згенерованою конфігурацією

Перевірити роботу функції на шаблоні templates/for.txt та даних із файлу
data_files/for.yml.

Важливий нюанс: каталог має бути отриманим із параметра template.
Не можна вказувати поточний каталог у FileSystemLoader - тобто НЕ треба
робити так FileSystemLoader("."). Вказівка поточного каталогу зламає роботу
інших завдань/тестів.

"""
import yaml


# так має виглядати виклик функції
if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))
