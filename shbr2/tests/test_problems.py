import pytest

from shbr2.a_repeating_number import has_repeats_at_dist
from shbr2.b_multicolor_sticks import count_sticks
from shbr2.c_replacing_words import replace_words
from shbr2.d_majority import majority
from shbr2.e_deleting_numbers import min_to_delete


@pytest.mark.parametrize(
    'a, max_dist, expected',
    (
        ([1, 2, 3, 1], 2, False),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ),
)
def test_a(a, max_dist, expected):
    assert has_repeats_at_dist(a, max_dist) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('R2G1R1B2G2', 1),
        ('R9G1B0', 0),
        ('R0G0B0R0G0B0R0G0B0', 1),
    ),
)
def test_b(test_input, expected):
    assert count_sticks(test_input) == expected


@pytest.mark.parametrize(
    'replacements, words, expected',
    (
        (
            ['a', 'b'],
            ['abdafb', 'basrt', 'casds', 'dsasa', 'a'],
            ['a', 'b', 'casds', 'dsasa', 'a'],
        ),
        (
            ['aa', 'bc', 'aaa'],
            ['a', 'aa', 'aaa', 'bcd', 'abcd'],
            ['a', 'aa', 'aa', 'bc', 'abcd'],
        ),
    ),
)
def test_c(replacements, words, expected):
    assert list(replace_words(words, replacements)) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([1, 2, 1], 1),
        ([7, 5, 5, 5, 5, 4, 5], 5),
        ([3, 3, 3, 1], 3),
    ),
)
def test_d(test_input, expected):
    assert majority(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([1, 2, 3, 4, 5], 3),
        ([1, 1, 2, 3, 5, 5, 2, 2, 1, 5], 4),
        ([1, 3, 5], 2),
        ([1], 0),
        ([1, 2], 0),
        ([1, 1, 1], 0),
    ),
)
def test_e(test_input, expected):
    assert min_to_delete(test_input) == expected
