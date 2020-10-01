import os
from pprint import pprint


def cook_book_create(file_path):
    cook_book = {}
    count_str = 0
    food = ''
    prop = ['ingredient_name', 'quantity', 'measure']
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line == '\n':
                count_str = 0
            else:
                if count_str == 0:
                    count_str += 1
                    food = line[:len(line) - 1]
                    cook_book[food] = []
                elif count_str == 1:
                    count_str += 1
                elif count_str == 2:
                    ingredient = line.split('|')
                    cook_book[food].append({prop[0]: ingredient[0].strip(), prop[1]: int(ingredient[1].strip()),
                                            prop[2]: ingredient[2].strip()[:len(ingredient[2]) - 1]})
        return cook_book


file_path = os.path.join(os.getcwd(), 'recipes.txt')
pprint(cook_book_create(file_path))