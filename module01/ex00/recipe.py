from pydantic import BaseModel, PositiveInt, Field
from typing import Literal


class Recipe(BaseModel):
    name: str = Field(
        description="name of the recipe"
    )
    cooking_lvl: int = Field(
        ge=1,
        le=5,
        description="level of cooking",
        example=3,
    )
    cooking_time: PositiveInt = Field(
        decription="time dedicate to cooking recipe in minutes",
        example=30,
    )
    ingredients: list[str] = Field(
        description="list of all ingredients recipe",
    )
    description: str | None = Field(
        description="information about recipe",
        default=''
    )
    recipe_type: Literal["lunch", "lunch", "dessert"] = Field(
        min_items=1,
        description="type of the recipe",
        example="lunch",
    )

    def __str__(self) -> str:
        """Returns the string to print with recipe's info"""
        string: str = (
            f'recipe\'s name:    {self.name}\n' +
            f'cooking level:    {self.cooking_lvl}\n' +
            f'cooking time:     {self.cooking_time}\n' +
            f'ingredients:      {self.ingredients}\n' +
            f'description:      {self.description}\n' +
            f'recipe_type:      {self.recipe_type}\n'
        )
        return string
