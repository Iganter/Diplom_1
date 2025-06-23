import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    'index, expected_name, expected_price',
    [
        (0, 'black bun', 100),
        (1, 'white bun', 200),
        (2, 'red bun', 300)
    ]
)
def test_available_buns_by_index(index, expected_name, expected_price):
    buns = Database().available_buns()
    bun = buns[index]
    assert isinstance(bun, Bun)
    assert bun.get_name() == expected_name
    assert bun.get_price() == expected_price


@pytest.mark.parametrize(
    'index, exp_type, exp_name, exp_price',
    [
        (0, INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (1, INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (2, INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (3, INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (4, INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (5, INGREDIENT_TYPE_FILLING, 'sausage', 300)
    ]
)
def test_available_ingredients_by_index(index, exp_type, exp_name, exp_price):
    ings = Database().available_ingredients()
    ing = ings[index]
    assert isinstance(ing, Ingredient)
    assert ing.get_type() == exp_type
    assert ing.get_name() == exp_name
    assert ing.get_price() == exp_price
