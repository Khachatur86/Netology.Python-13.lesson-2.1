# Исправление
def get_shop_list_by_dishes(dishes, person_count, cook_book_list):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book_list[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list(cook_book_list):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book_list)
    print_shop_list(shop_list)


def read_receipts():
    cook_book = {}
    with open("receipts.txt", encoding="utf-8") as f:
        for line in f:  # Итерирование по строкам
            dish = line.lower().strip()  # присвоение значения строки наименованию блюда
            ingredients_quantity = int(f.readline().strip())
            dishes = []
            for i in range(ingredients_quantity):
                dishes_list = f.readline().split("|")
                dishes_dict = {'ingridient_name': dishes_list[0].strip(), 'quantity': int(dishes_list[1].strip()),
                               'measure': dishes_list[2].strip()}
                dishes.append(dishes_dict)
            f.readline()
            cook_book[dish] = dishes
    return cook_book


cook_book_list = read_receipts()
create_shop_list(cook_book_list)
