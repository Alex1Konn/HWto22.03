"""
3. Список объектов в JSON Создайте список из 3 книг (название, автор, год).
Сохраните в books.json.
Добавьте новую книгу и перезапишите файл.
"""

import json
books = [
    {
        "title": "Война и мир",
        "author": "Лев Толстой",
        "year": 1869
    },
    {
        "title": "Преступление и наказание",
        "author": "Федор Достоевский",
        "year": 1866
    },
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "year": 1967
    }
]

filename = 'books.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

new_book = {
    "title": "1984",
    "author": "Джордж Оруэлл",
    "year": 1949
}
books.append(new_book)

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(books, f, ensure_ascii=False, indent=4)

print(f"В файл {filename} добавлена книга. Всего книг: {len(books)}")



"""
4. Фильтрация CSV-данных Прочитайте CSV с товарами (название, цена, количество). 
Отфильтруйте товары с ценой > 1000 рублей. 
Запишите их в expensive.csv.
"""

import csv
source_file = 'products.csv'
data = [
    ['name', 'price', 'quantity'],
    ['Ноутбук', '50000', '5'],
    ['Мышка', '800', '20'],
    ['Клавиатура', '2500', '15'],
    ['Монитор', '15000', '7'],
    ['Коврик', '500', '50'],
    ['Наушники', '1200', '10']
]

expensive_products = []

with open(source_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

with open(source_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        price = int(row['price'])

        if price > 1000:
            expensive_products.append(row)
print(len(expensive_products))

output_file = 'expensive.csv'
fieldnames = ['name', 'price', 'quantity']
with open(output_file, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expensive_products)


"""
1. Запись словаря в JSON-файл Создайте словарь с 
данными пользователя (имя, возраст, email). 
Запишите его в файл user.json с отступами.
Прочитайте файл обратно и выведите данные.
"""


import json
from pprint import pprint

filename = 'user.json'

person_data = [
    {"name": "Ivan Ivanov", "age": 20, "email": "example@mail.ru"},
    {"name": "Petr Petrov", "age": 30, "email": "example34@mail.ru"},
    {"name": "Dmitry Belov", "age": 40, "email": "example43@mail.ru"}
    ]

with open(filename, "w", encoding="utf-8") as file:
    file.write(json.dumps(person_data, ensure_ascii=False, indent=4))

with open(filename, encoding="utf-8") as file:
    person_data_2 = json.loads(file.read())

pprint(person_data_2)

"""
2. Запись списка в CSV-файл Создайте список из 3–5 студентов (имя, оценка, предмет). Запишите в students.csv с заголовком. Прочитайте файл и выведите строки.
"""

import csv

filename = 'students.csv'

students_list = [
    {"name": "Ivan Ivanov", "grade": 10, "subject": "Math"},
    {"name": "Petr Petrov", "grade": 12, "subject": "Math"},
    {"name": "Dmitry Belov", "grade": 12, "subject": "Math"}
]
with open(filename, 'w', encoding='utf-8',newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(["Name", "Grade", "Subject"])

    for student in students_list:
        writer.writerow([student["name"], student["grade"], student["subject"]])
        writer.writerow(["Ivan Ivanov", 10, "Math"])

with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

for row in rows:
    print(row)