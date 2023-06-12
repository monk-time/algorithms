import pytest

from extra.a_steps import steps
from extra.b_canonical_path import get_canonical_path
from extra.c_buy_sell import find_max_difference


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 3),
        (7, 3),
        (8, 3),
    ),
)
def test_a(test_input, expected):
    assert steps(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('/home/', '/home'),
        ('/../', '/'),
        ('/home//foo/', '/home/foo'),
    ),
)
def test_b(test_input, expected):
    assert get_canonical_path(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([10, 3, 5, 3, 11, 9], (2, 5)),
        ([5, 5, 5, 5], (0, 0)),
        ([1], (0, 0)),
        ([4, 3, 2, 1], (0, 0)),
        ([9, 10, 1, 5], (3, 4)),
        ([1, 10, 2, 5], (1, 2)),
        ([10, 2, 9, 1], (2, 3)),
        ([9, 7, 4, 5, 6, 3, 1], (3, 5)),
        ([9, 7, 4, 5, 6, 3, 1, 2], (7, 8)),
    ),
)
def test_c(test_input, expected):
    assert find_max_difference(test_input) == expected
