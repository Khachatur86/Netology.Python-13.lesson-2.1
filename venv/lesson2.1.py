
def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=
          new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)


# Создание словаря аналогичного исходному в лекции 1.5
# Создадим пустой словарь, в качестве ключей будут наименования блюд. А в качестве значения - список.
# Список будет состоять из словаря, в котором будет отражаться информация - имя ингредиента, количество, мера веса.
# В первой строке - наименование блюда, во второй количество ингредиентов, с начиная с третьей и далее - наименование ингредиента,
# количество ингредиента, и вес ингредиента
#1. Чтение файла (with () as f...
#2. Проитеруемся циклом for по файлу,  значение первой строки присвоим наименованию блюда.
#3. Значениями начиная с третьей строки сформируем словари по ингредиентам, количеству и мере.
#4. Сформируем словарь.


def read_receipts():
  cook_book = {}
  with open("reciepts.txt", encoding="utf-8") as f:
    for line in f:# Итерирование по строкам
      dish = line.lower().strip()# присвоение значения строки наименованию блюда
      ingredients_quantity = int(f.readline().strip())
      dishes = []
      for i in range(ingredients_quantity):
        dishes_list = f.readline().split("|").strip()
        dishes_dict = {'ingridient_name': dishes_list[0], 'quantity':dishes_list[1], 'measure': dishes_list[2]}
        dishes.append(dishes_dict)
      f.readline()
      cook_book[dish] = dishes
  return cook_book

cook_book = read_receipts()
create_shop_list()
        
