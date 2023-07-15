import pytest

from shbr5.a_bulls_and_cows import count_bulls_and_cows
from shbr5.b_largest_substring import find_max_good_substring_length
from shbr5.c_mountains import find_peak
from shbr5.d_delete_string import min_length_after_ops
from shbr5.e_pitcraft import count_filled_blocks


@pytest.mark.parametrize(
    'test_input, expected',
    ((('1370', '7311'), (1, 2)),),
)
def test_a(test_input, expected):
    assert count_bulls_and_cows(*test_input) == expected


@pytest.mark.parametrize(
    's, min_count, expected',
    (
        ('aaabb', 3, 3),
        ('ababbc', 2, 5),
        ('aaabb', 4, 0),
        ('aaabbb', 0, 6),
        ('aaabbb', 1, 6),
        ('aaabbb', 2, 6),
        ('aaabbb', 3, 6),
        ('aaabbb', 4, 0),
        ('adbacbacaaacccb', 2, 13),
        ('adbacbacaaacccb', 4, 8),
        ('abacc', 2, 2),
    ),
)
def test_b(s, min_count, expected):
    assert find_max_good_substring_length(s, min_count) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([1, 2, 1], 2),
        ([1, 2, 3, 1], 3),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1], 5),
        ([1, 2, 3, 4, 5, 1], 5),
        ([1, 5, 4, 3, 2, 1], 2),
    ),
)
def test_c(test_input, expected):
    assert find_peak(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('abba', 0),
        ('aboba', 1),
        ('zzzaabxxxcazz', 5),
    ),
)
def test_d(test_input, expected):
    assert min_length_after_ops(test_input) == expected


sample_filetree = [
    'emoh',
    ' vonavi',
    '  a.doc',
    '  b.doc',
    ' vortep',
    '  .bashrc',
    ' vorodis',
    '  onrop',
    '   1.avi',
    '   2.avi',
    'top.doc',
    'rav',
    ' bil',
]


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [2, 5, 2, 3, 6, 9, 3, 1, 3, 4, 6],
            18,
        ),
        (
            [1, 4, 3, 1, 5, 1, 7, 5, 2, 3, 6, 7, 10, 3, 7, 13, 5, 3, 8, 6, 4],
            38,
        ),
    ),
)
def test_e(test_input, expected):
    assert count_filled_blocks(test_input) == expected
