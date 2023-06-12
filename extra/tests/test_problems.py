import pytest

from extra.c_buy_sell import find_max_difference


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([10, 3, 5, 3, 11, 9], (2, 5)),
        ([5, 5, 5, 5], (0, 0)),
        ([1], (0, 0)),
        ([9, 10, 1, 5], (3, 4)),
        ([1, 10, 2, 5], (1, 2)),
    ),
)
def test_c(test_input, expected):
    assert find_max_difference(test_input) == expected
