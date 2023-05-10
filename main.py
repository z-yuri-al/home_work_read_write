from pprint import pprint

with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        count_ingredient = int(file.readline())
        ingredient_list = []
        for _ in range(count_ingredient):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredient_dict = {
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            }
            ingredient_list.append(ingredient_dict)
        file.readline()
        cook_book[dish_name] = ingredient_list

    pprint(cook_book, sort_dicts=False)

print()
print()

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        recipe = cook_book[dish]
        for ingridient in recipe:
            key = ingridient['ingredient_name']
            if key not in result:
                new_dict = {
                    'measure' : ingridient['measure'],
                    'quantity' : int(ingridient['quantity']) * person_count

                }
                result[key] = new_dict
            else:
                result[key]['quantity'] += int(ingridient['quantity']) * person_count

    pprint(result, sort_dicts=False)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)


#ЗАДАНИЕ 3

with open('sorted/1.txt') as file1, open('sorted/2.txt') as file2, open('sorted/3.txt') as file3, open('sorted/new.txt', 'w') as new_file:
    print(file2.read())
    dict_file = {
        file1 : len(file1.readlines()),
        file2 : len(file2.readlines()),
        file3 : len(file3.readlines())
    }


    dict_file_sort = dict(sorted(dict_file.items(), key=lambda item: item[1]))
    pprint(dict_file_sort, sort_dicts=False)
    print()


    print(file2.read())

    for file, len_file in dict_file_sort.items():
        new_file.writelines('file_name\n')
        new_file.writelines(f'{len_file}\n')
        for line in file.readlines():
            new_file.writelines(f'{line}\n')







