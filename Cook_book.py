from pprint import pprint
with open('1.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_count = int(file.readline())
        print(ingredient_count)
        ingredients = []
        for a in range(ingredient_count):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure
                }
            )
        cook_book[dish] = ingredients
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = []
    for dish in dishes:
        if dish in cook_book:
            ingr_list.extend(cook_book[dish])
    # print(ingr_list)
    ingredient_dish_list = {}
    for ingr in ingr_list:
        if ingr['ingredient_name'] not in ingredient_dish_list:
            ingredient_dish_list[ingr['ingredient_name']] = {'measure': ingr['measure'],
                                                             'quantity': ingr['quantity'] * int(person_count)}
        else:
            ingredient_dish_list[ingr['ingredient_name']] = ingredient_dish_list[ingr['ingredient_name']]['quantity'] + \
                                                            ingr['quantity'] * int(person_count)

    return ingredient_dish_list


pprint(get_shop_list_by_dishes(all_dishes, 5))
