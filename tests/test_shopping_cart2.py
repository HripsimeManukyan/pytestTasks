import pytest
import source.shopping_cart as shopping_cart


# @pytest.fixture
# def sample_items():
#     return {"apple": 1.0,
#             "kiwi": 0.5,
#             "orange": 1.5}
#
#
# def test_calculate_total_single_item(sample_items):
#     items = {"apple": 1.0}
#     assert shopping_cart.calculate_total(items) == 1.0
#
#
# def test_calculate_total_multiple_items(sample_items):
#     items = {"apple": 1.0, "kiwi": 0.5, "orange": 1.5}
#     assert shopping_cart.calculate_total(items) == 3.0
#
#
# def test_calculate_total_empty_items(sample_items):
#     items = {}
#     assert shopping_cart.calculate_total(items) == 0
#
#
# @pytest.mark.parametrize("items, expected_total", [
#     ({}, 0),
#     ({"apple": 1.0}, 1.0),
#     ({"apple": 1.0, "kiwi": 0.5}, 1.5),
#     ({"apple": 1.0, "kiwi": 0.5, "orange": 1.5}, 3.0)
# ])
# def test_calculate_total_parameterized(items, expected_total):
#     assert shopping_cart.calculate_total(items) == expected_total
#
#
# def test_calculate_total_invalid_item_price(sample_items):
#     items =[{"kiwi": -0.5}]
#     with pytest.raises(ValueError):
#         shopping_cart.calculate_total(items)


@pytest.fixture
def sample_items():
    return {
        "apple": 1.0,
        "banana": 0.5,
        "orange": 1.5
    }

def test_calculate_total_single_item(sample_items):
    items = {"apple": 1.0}
    assert shopping_cart.calculate_total(items) == 1.0

def test_calculate_total_multiple_items(sample_items):
    items = {"apple": 1.0, "banana": 0.5, "orange": 1.5}
    assert shopping_cart.calculate_total(items) == 3.0

def test_calculate_total_empty_cart(sample_items):
    items = {}
    assert shopping_cart.calculate_total(items) == 0

@pytest.mark.parametrize("items, expected_total", [
    ({}, 0),
    ({"apple": 1.0}, 1.0),
    ({"apple": 1.0, "banana": 0.5}, 1.5),
    ({"apple": 1.0, "banana": 0.5, "orange": 1.5}, 3.0)
])
def test_calculate_total_parameterized(items, expected_total):
    assert shopping_cart.calculate_total(items) == expected_total

def test_calculate_total_invalid_item_price(sample_items):
    items = {"apple": -1.0}  # negative price
    with pytest.raises(ValueError):
        shopping_cart.calculate_total(items)