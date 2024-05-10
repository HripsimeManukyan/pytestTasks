import pytest


# @pytest.fixture
# def take_value():
#     i = 20
#     return i
#
#
# def test_one(take_value):
#     assert take_value - 10 == 10
#
#
# def test_two(take_value):
#     assert take_value - 4 == 5

# @pytest.mark.parametrize("n, expected",[(5,50), (6,60),(7,21)])
# def test_mul(n, expected):
#     assert 10*n == expected

import math
def test_add_fail():
    n = 20
    assert n+n == 40

def test_sr_fail():
    n = 9
    assert math.sqrt(n) ==2


def test_m_fail():
    assert 6*5 == 31




