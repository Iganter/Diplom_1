import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import IngredientData


class TestIngredientSauce:

    @pytest.mark.parametrize("name, price", IngredientData.SAUCE_CASES)
    def test_get_type(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ing.get_type() == INGREDIENT_TYPE_SAUCE

    @pytest.mark.parametrize("name, price", IngredientData.SAUCE_CASES)
    def test_get_name(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ing.get_name() == name

    @pytest.mark.parametrize("name, price", IngredientData.SAUCE_CASES)
    def test_get_price(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert ing.get_price() == price


class TestIngredientFilling:

    @pytest.mark.parametrize("name, price", IngredientData.FILLING_CASES)
    def test_get_type(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ing.get_type() == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize("name, price", IngredientData.FILLING_CASES)
    def test_get_name(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ing.get_name() == name

    @pytest.mark.parametrize("name, price", IngredientData.FILLING_CASES)
    def test_get_price(self, name, price):
        ing = Ingredient(INGREDIENT_TYPE_FILLING, name, price)
        assert ing.get_price() == price
