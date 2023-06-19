import pytest

from extra.a_steps import steps
from extra.b_canonical_path import get_canonical_path
from extra.c_buy_sell import find_max_difference
from extra.d_time_difference import min_gap
from extra.e_break_palindrome import break_palindrome


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
        ([1001, 2000], (1, 2)),
        ([6, 9, 8, 3, 4], (1, 2)),
        ([9, 4, 8, 3, 6], (2, 3)),
        ([3, 5, 8, 1, 5], (4, 5)),
    ),
)
def test_c(test_input, expected):
    assert find_max_difference(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (['23:59', '00:00'], 1),
        (['00:00', '23:59', '00:00'], 0),
        (['23:30', '00:30'], 60),
        (['14:40', '14:51'], 11),
        (['14:40', '15:51', '20:00'], 71),
    ),
)
def test_d(test_input, expected):
    assert min_gap(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('abba', 'aaba'),
        ('a', ''),
        ('bbb', 'abb'),
        ('cadac', 'aadac'),
        ('', ''),
        ('aaaa', 'aaab'),
        ('aba', 'abb'),
        ('aabaa', 'aabab'),
    ),
)
def test_e(test_input, expected):
    assert break_palindrome(test_input) == expected
