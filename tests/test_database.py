import pytest
from praktikum.database import Database
from praktikum.datasets import list_buns, list_ingredients


class TestDatabase:
   
    @pytest.mark.parametrize('buns_from_list', [list_buns])
    def test_available_buns_add_buns_returns_list_with_buns(self, buns_from_list):
        database = Database()
        buns = database.available_buns()
        for i in range(len(buns_from_list)):
            correct_name, correct_price = buns_from_list[i]
            assert buns[i].name == correct_name 
            assert buns[i].price == correct_price
         

    @pytest.mark.parametrize('ingredients_from_list', [list_ingredients])
    def test_available_ingredients_add_ingredients_returns_list_with_ingredients(self, ingredients_from_list):
        database = Database()
        ingredients = database.available_ingredients()
        for i in range(len(ingredients_from_list)):
            correct_name, correct_type, correct_price = ingredients_from_list[i]
            assert ingredients[i].name == correct_name 
            assert ingredients[i].get_type() == correct_type
            assert ingredients[i].get_price() == correct_price
            