import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    'ingredient_type, name, price',
    [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_SAUCE, 'sour cream', 200),
        (INGREDIENT_TYPE_SAUCE, 'chili sauce', 300),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 100),
        (INGREDIENT_TYPE_FILLING, 'dinosaur', 200),
        (INGREDIENT_TYPE_FILLING, 'sausage', 300)
    ]
)
def test_ingredient_get_type_and_name_and_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
