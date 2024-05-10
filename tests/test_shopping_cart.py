import pytest
import source.shopping_cart as shopping_cart


def test_calculate_total_single_item():
    items = [{"shoes": 5000}]
    total_cost = shopping_cart.calculate_total(items)
    assert total_cost == 5000


def test_calculate_total_multiple_items():
    items = [{"shoes": 2000}, {"bag": 7000}, {"hat": 1000}]
    total_cost = shopping_cart.calculate_total(items)
    assert total_cost == 10000


def test_calculate_total_empty_cart():
    items = [{}, {}, {}]
    total_cost = shopping_cart.calculate_total(items)
    assert total_cost == 0

def test_calculate_total_invalid_item_price():
    items = [{"shoes": 300}, {"bag": 900}]
    total_cost = shopping_cart.calculate_total(items)
    assert total_cost == 1200


