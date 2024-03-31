import pytest

from yaintern.a_usb import min_price
from yaintern.b_even_fence import min_minmax_diff
from yaintern.c_repo_inheritance import make_tree, max_depth
from yaintern.d_digs_and_tiles import Dig, min_sadness
from yaintern.e_priority_admission import enroll


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ((1, 3, 1, 10), 2),
        ((2, 4, 9, 10), 10),
        ((3, 8, 9, 10), 19),
    ),
)
def test_a(test_input, expected):
    assert min_price(*test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (([15, 19], 0), 4),
        (([1, 11, 6, 41, 15, 13, 14], 2), 9),
    ),
)
def test_b(test_input, expected):
    assert min_minmax_diff(*test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ((0, 0, 1), 3),
        ((0, 1, 2, 0, 4, 5, 6, 4), 7),
    ),
)
def test_c(test_input, expected):
    leaves = make_tree(test_input)
    assert max_depth(leaves) == expected


@pytest.mark.parametrize(
    'digs, sidewalk_count, laying_count, expected',
    (
        (
            (
                (1, 2),
                (2, 3),
                (2, 1),
                (6, 2),
            ),
            5,
            3,
            5,
        ),
        (
            (
                (1, 1),
                (1, 2),
                (3, 1),
                (4, 2),
            ),
            2,
            2,
            5,
        ),
    ),
)
def test_d(digs, sidewalk_count, laying_count, expected):
    digs = [Dig(*dig) for dig in digs]
    assert min_sadness(digs, sidewalk_count, laying_count) == expected


@pytest.mark.parametrize(
    'program_spots, priorities, expected',
    (
        (
            [1, 5],
            (
                (3, 1, 1),
                (1, 1, 2),
                (2, 2, 1, 2),
                (3, 2, 1, 2),
            ),
            [-1, 2, 1, 2],
        ),
    ),
)
def test_e(program_spots, priorities, expected):
    assert enroll(program_spots, priorities) == expected
