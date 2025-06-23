import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger


def test_set_buns_assigns_bun():
    bun_mock = Mock(spec=Bun)
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.bun is bun_mock


def test_add_ingredient_appends_to_list():
    ing_mock = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ing_mock)
    assert burger.ingredients == [ing_mock]


def test_remove_ingredient_removes_from_list():
    ing1 = Mock(spec=Ingredient)
    ing2 = Mock(spec=Ingredient)
    burger = Burger()
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    burger.remove_ingredient(0)
    assert burger.ingredients == [ing2]


def test_get_price_without_ingredients():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 5.0
    burger = Burger()
    burger.set_buns(bun_mock)
    assert burger.get_price() == 10.0


def test_get_price_with_ingredients():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_price.return_value = 5.0
    burger = Burger()
    burger.set_buns(bun_mock)

    ing1 = Mock(spec=Ingredient)
    ing1.get_price.return_value = 1.0
    ing2 = Mock(spec=Ingredient)
    ing2.get_price.return_value = 2.0

    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)
    assert burger.get_price() == 13.0


@pytest.mark.parametrize(
    'initial_names, source_index, destination_index, expected_names',
    [
        (['Lettuce', 'Tomato', 'Onion'], 0, 2, ['Tomato', 'Onion', 'Lettuce']),
        (['Patty', 'Cheese', 'Bacon', 'Pickle'], 3, 1, ['Patty', 'Pickle', 'Cheese', 'Bacon'])
    ]
)
def test_move_ingredient_reorders(initial_names, source_index, destination_index, expected_names):
    burger = Burger()
    burger.set_buns(Mock(spec=Bun))
    burger.ingredients = [
        Mock(spec=Ingredient, get_name=Mock(return_value=name), get_price=Mock(return_value=0))
        for name in initial_names
    ]

    burger.move_ingredient(source_index, destination_index)
    result_names = [ing.get_name() for ing in burger.ingredients]
    assert result_names == expected_names


def test_get_receipt_format_and_values():
    bun_mock = Mock(spec=Bun)
    bun_mock.get_name.return_value = 'TestBun'
    bun_mock.get_price.return_value = 3.0

    sauce = Mock(spec=Ingredient)
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    sauce.get_name.return_value = 'Hot'
    sauce.get_price.return_value = 1.0

    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    filling.get_name.return_value = 'Meat'
    filling.get_price.return_value = 4.0

    burger = Burger()
    burger.set_buns(bun_mock)
    burger.add_ingredient(sauce)
    burger.add_ingredient(filling)

    receipt = burger.get_receipt().split('\n')
    assert receipt[0] == '(==== TestBun ====)'
    assert receipt[1] == '= sauce Hot ='
    assert receipt[2] == '= filling Meat ='
    assert receipt[3] == '(==== TestBun ====)'
    assert receipt[4] == ''
    assert receipt[5] == f'Price: {burger.get_price()}'
