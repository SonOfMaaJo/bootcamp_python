from typing_extensions import TypedDict
from typing import List


class Recipe(TypedDict):
    ingredients: List[str]
    meal: str
    prep_time: int


cookbook: dict[str, Recipe] = {
    "Sandwich": {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": 'lunch',
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": 'dessert',
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": 'lunch',
        "prep_time": 15,
    },
}


def display_all_recipe_name() -> None:
    """function that display content of cookbook"""
    for key in cookbook:
        print(f'{key}')


def print_detail_recipe(name: str) -> None:
    """function that print detail about recipe of cookbook"""
    print('ingredients:', *cookbook[name]["ingredients"], '\n', sep='\n')
    print('type of meal:\n', *cookbook[name]["meal"])
    print('preparation time:', cookbook[name]["prep_time"], sep='\n')


def delete_recipe(name: str) -> None:
    """function to delete recipe from cookbook"""
    del cookbook[name]


def add_recipe() -> None:
    """function to add recipe in cookbook"""
    name: str = input('Enter a name:\n>> ')
    ingredients: List[str] = []
    meal: str
    prep_time: int
    c = input('Enter ingredients:\n>> ')
    while c != '':
        ingredients.append(c)
        c = input('>> ')
    meal = input('Enter a meal type:\n>> ')
    try:
        prep_time = int(input('Enter a preparation time:\n>> '))
        if prep_time < 0:
            raise ValueError()
        cookbook.update(
            {
                name: {
                    'ingredients': ingredients,
                    'meal': meal,
                    'prep_time': prep_time,
                }
            }
        )
    except ValueError:
        print('AssertionError: preparation time should be an positive integer')


if __name__ == '__main__':
    print('Welcome to the Python Cookbook !')
    while True:
        print('List of available options:',
              ' 1: Add a recipe',
              ' 2: Delete a recipe',
              ' 3: Print a recipe',
              ' 4: Print the cookbook',
              ' 5: Quit',
              '\n',
              'Please select an option:', sep='\n')
        try:
            option = int(input('>> '))
            if option < 1 or option > 5:
                raise ValueError()
            print('')
        except ValueError:
            print('')
            print('Sorry, this option does not exist.')
            continue
        if option == 5:
            print('Cookbook closed. Goodbye !')
            break
        elif option == 1:
            add_recipe()
            print('')
        elif option == 2:
            try:
                delete_recipe(input('Enter a name:\n>> '))
                print('')
            except KeyError:
                print('\nThis recipe doesn\'t exist,',
                      'select option 4 to have current available recipe.\n')
                continue
        elif option == 3:
            try:
                print_detail_recipe(input('Enter a recipe\'s name:\n>> '))
                print('')
            except KeyError:
                print('\nThis recipe deosn\'t exist,'
                      'select option 4 to have current available recipe.\n')
        elif option == 4:
            display_all_recipe_name()
