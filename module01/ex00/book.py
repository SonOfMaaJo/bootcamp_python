from pydantic import BaseModel, Field, PastDatetime
from recipe import Recipe
from datetime import datetime


class Book(BaseModel):
    name: str = Field(
        description="the name of the book"
    )
    last_update: PastDatetime = Field(
        description="the date of the last update"
    )
    creation_date: PastDatetime = Field(
        description="the creation date of the book"
    )
    recipes_list: dict[str, list[Recipe]] = {
        "starter": [],
        "lunch": [],
        "dessert": [],
    }

    def get_recipe_by_name(self, name: str) -> Recipe | None:
        """Prints a recipe with the name \texttt{name}
        and returns the instance
        """
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    str(recipe)
                    return recipe
        print("The recipe doesn't exists.")
        return None

    def get_recipes_by_types(self, recipe_type: str) -> list[Recipe] | None:
        """Gets all recipes names for a given recipe_type"""
        if recipe_type not in self.recipes_list:
            return None
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe: Recipe) -> None:
        """Adds a recipe to the book and updates last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
