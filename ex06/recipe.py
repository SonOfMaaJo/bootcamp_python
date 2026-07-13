from typing import TypedDict


class Recipe(TypedDict):
    ingredients: list[str]
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
