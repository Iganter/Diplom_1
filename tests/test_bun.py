import pytest
from praktikum.bun import Bun
from data import BunData


class TestBun:

    @pytest.mark.parametrize("name, price", BunData.CASES)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BunData.CASES)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
