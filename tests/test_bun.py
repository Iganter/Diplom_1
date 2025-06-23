import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name, price', [
    ('Classic Bun', 50.0),
    ('Black Bun', 75.5)
])
def test_bun_get_name_and_price_successful(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
