import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import DatabaseData


class TestDatabase:

    @pytest.mark.parametrize('index, expected_name, expected_price', DatabaseData.BUN_CASES)
    def test_available_buns_by_index(self, index, expected_name, expected_price):
        buns = Database().available_buns()
        bun = buns[index]
        assert isinstance(bun, Bun)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize('index, exp_type, exp_name, exp_price', DatabaseData.INGREDIENT_CASES)
    def test_available_ingredients_by_index(self, index, exp_type, exp_name, exp_price):
        ings = Database().available_ingredients()
        ing = ings[index]
        assert isinstance(ing, Ingredient)
        assert ing.get_type() == exp_type
        assert ing.get_name() == exp_name
        assert ing.get_price() == exp_price
