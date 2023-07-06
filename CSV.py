import csv

# with open('sq.csv', 'w', newline='', encoding='utf-8') as f:            # Каждая строка представлена списком . Создаем файл
#     write = csv.writer(f, delimiter=';', quotechar='"',
#                        quoting=csv.QUOTE_MINIMAL)
#
#     for i in range(10):
#         write.writerow([i, i ** 2, f'Квадрат числа{i} = {i ** 2}'])     # 3 Элемента в файле

# with open('sq.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=';', quotechar='"')
#     for i in reader:
#         x, y, z = i
#         print(x, y, z)


# goods = [('Ковер', 5000), ('телевизор', 3000), ('Кресло', 1500), ('Стол', 2500), ('Холодильник', 4850)]
# with open('goods.csv', 'w', newline='', encoding="utf-8") as f:
#     writer = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for i in goods:
#         writer.writerow(i)
#         #print(i)
#
# with open('goods.csv', 'r', encoding='utf-8') as f:
#      reader = csv.reader(f, delimiter=';', quotechar='"')
#      for i in reader:
#         x, y = i
#         #print(x, y)


data = [{
    'lastname': 'Салем',
    'firstname': 'Борис',
    'class_number': 9,
    'class_letter': 'А'
}, {
    'lastname': 'Пушкин',
    'firstname': 'Виталик',
    'class_number': 9,
    'class_letter': 'Б'
}]
with open('form.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=list(data[0].keys()),
                            delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()
    for item in data:
        writer.writerow(item)


with open('form.csv', 'r', encoding='utf-8') as f:
      reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
      #header = next(reader)
      for item in reader:
          for x, y in item.items():
              print(x, y)
