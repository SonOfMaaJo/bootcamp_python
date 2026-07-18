from book import Book
from recipe import Recipe
from datetime import datetime
from time import sleep

if __name__ == '__main__':
    # recipes_list: dict[str, list[Recipe]] = {
    #     "starter": [],
    #     "lunch": [],
    #     "dessert": [],
    # }
    date = datetime.now()
    book = Book(name="mybook", last_update=date,
                creation_date=date)
    print('-'*50)
    print('Creation date of the book: ', book.creation_date)
    print(f'lunch type: {book.recipes_list["lunch"]}')
    book.add_recipe(Recipe(name="Okok", cooking_lvl=1, cooking_time=60,
                           ingredients=["waterleef", "Oignons"],
                           description="cameroonian recipe",
                           recipe_type="lunch"))
    sleep(2)
    print('-'*50)
    print('first update: ', book.last_update)
    book.add_recipe(Recipe(name="Cake", cooking_lvl=1, cooking_time=20,
                           ingredients=["milk", "salt"],
                           recipe_type="lunch"))
    print('-'*50)
    print('second update: ', book.last_update)
    lunch = book.get_recipes_by_types("lunch")
    for recipe in lunch:
        print(book.get_recipe_by_name(recipe.name))
