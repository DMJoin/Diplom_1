import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *

list_buns = [
    ("black bun", 100),
    ("white bun", 200), 
    ("red bun", 300)
]

list_ingredients = [
    ("hot sauce", INGREDIENT_TYPE_SAUCE, 100),
    ("sour cream", INGREDIENT_TYPE_SAUCE, 200),
    ("chili sauce", INGREDIENT_TYPE_SAUCE, 300),
    ("cutlet", INGREDIENT_TYPE_FILLING, 100),
    ("dinosaur", INGREDIENT_TYPE_FILLING, 200),
    ("sausage", INGREDIENT_TYPE_FILLING, 300),
]


classic_bun = Bun("Классическая", 50)
ingredient_ketchup = Ingredient("Кетчуп", "соус", 100)
ingredient_cutlet = Ingredient("Котлета", "начинка", 300)