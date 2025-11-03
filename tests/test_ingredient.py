import pytest

class TestIngredient:

    def test_ingredient_name_price_type_return_correct(self, mock_ingredient_data):
        assert mock_ingredient_data.get_type() == "начинка"
        assert mock_ingredient_data.get_name() == "Котлета"
        assert mock_ingredient_data.get_price() == 250