class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int,
                 ingredients: list[str], description: str, recipe_type: str):
        """Use to initialize the recipe value"""
        if not isinstance(name, str):
            raise ValueError('ValueError: attribute name should be str'
                             f'but find {type(name)}')
        if not (isinstance(cooking_lvl, int) or cooking_lvl > 5) \
                or cooking_lvl < 1:
            raise ValueError('ValueError: attribute cooking_lvl should be int'
                             f'but find {type(cooking_lvl)}')
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError('ValueError: attribute cooking_time should be int'
                             f'but find {type(cooking_time)}')
        if not isinstance(ingredients, list):
            raise ValueError('ValueError: attribute ingredients should be list'
                             f'but find {type(ingredients)}')
        if description != '' and not isinstance(description, str):
            raise ValueError('ValueError: attribute description should be str'
                             f'but found {type(description)}')
        if not isinstance(recipe_type, str) or recipe_type not in ['starter',
                                                                   'lunch',
                                                                   'dessert']:
            raise ValueError('ValueError: attribute recipe_type should be',
                             'either starter, lunch, or dessert')
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self) -> str:
        """Returns the string to print with recipe's info"""
        string: str = (
            f'recipe\'s name :  {self.name}\n' +
            f'cooking level:    {self.cooking_lvl}\n' +
            f'cooking time :    {self.cooking_time}' +
            f'ingredients:      {self.ingredients}' +
            f'description:      {self.description}' +
            f'recipe_type:      {self.recipe_type}'
        )
        return string
