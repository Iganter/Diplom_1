import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from data import BurgerData


class TestBurger:

    def test_set_buns_assigns_bun(self):
        bun = Mock(spec=Bun)
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient_appends_to_list(self):
        ing = Mock(spec=Ingredient)
        burger = Burger()
        burger.add_ingredient(ing)
        assert burger.ingredients == [ing]

    def test_remove_ingredient_removes_from_list(self):
        ing1, ing2 = Mock(spec=Ingredient), Mock(spec=Ingredient)
        burger = Burger()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.remove_ingredient(0)
        assert burger.ingredients == [ing2]

    def test_get_price_without_ingredients(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 5.0
        burger = Burger()
        burger.set_buns(bun)
        assert burger.get_price() == 10.0

    def test_get_price_with_ingredients(self):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = 5.0
        ing1 = Mock(spec=Ingredient)
        ing1.get_price.return_value = 1.0
        ing2 = Mock(spec=Ingredient)
        ing2.get_price.return_value = 2.0

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)

        assert burger.get_price() == 13.0

    @pytest.mark.parametrize("initial_names, source_index, destination_index, expected_names", BurgerData.MOVE_CASES)
    def test_move_ingredient_reorders(self, initial_names, source_index, destination_index, expected_names):
        burger = Burger()
        burger.set_buns(Mock(spec=Bun))
        burger.ingredients = [
            Mock(spec=Ingredient, get_name=Mock(return_value=name), get_price=Mock(return_value=0))
            for name in initial_names
        ]

        burger.move_ingredient(source_index, destination_index)
        result = [i.get_name() for i in burger.ingredients]
        assert result == expected_names

    def test_get_receipt_format_and_values(self):
        bun = Mock(spec=Bun)
        bun.get_name.return_value = BurgerData.RECEIPT_BUN_NAME
        bun.get_price.return_value = BurgerData.RECEIPT_BUN_PRICE

        sauce_name, sauce_price = BurgerData.RECEIPT_INGREDIENTS[0][1], BurgerData.RECEIPT_INGREDIENTS[0][2]
        sauce = Mock(spec=Ingredient)
        sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
        sauce.get_name.return_value = sauce_name
        sauce.get_price.return_value = sauce_price

        fill_name, fill_price = BurgerData.RECEIPT_INGREDIENTS[1][1], BurgerData.RECEIPT_INGREDIENTS[1][2]
        filling = Mock(spec=Ingredient)
        filling.get_type.return_value = INGREDIENT_TYPE_FILLING
        filling.get_name.return_value = fill_name
        filling.get_price.return_value = fill_price

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(filling)

        receipt = burger.get_receipt().split("\n")
        assert receipt[0] == f"(==== {BurgerData.RECEIPT_BUN_NAME} ====)"
        assert receipt[3] == f"(==== {BurgerData.RECEIPT_BUN_NAME} ====)"
        assert receipt[1] == f"= sauce {sauce_name} ="
        assert receipt[2] == f"= filling {fill_name} ="
        assert receipt[4] == ""
        assert receipt[5] == f"Price: {burger.get_price()}"
