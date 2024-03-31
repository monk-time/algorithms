import random
from io import StringIO
from itertools import cycle, islice

import pytest

from sprint3.a_bracket_gen import bracket_gen
from sprint3.b_combinations import phone_combinations, phone_combinations_rec
from sprint3.c_subsequence import is_subsequence
from sprint3.d_cookies import count_happy
from sprint3.e_houses import count_houses, count_houses_acc
from sprint3.f_triangle import max_perimeter
from sprint3.final_broken_search import broken_search
from sprint3.final_efficient_quicksort import main, quicksort
from sprint3.g_wardrobe import counting_sort
from sprint3.h_large_number import largest_number
from sprint3.i_conference_fans import top_k_schools
from sprint3.j_bubble import run_bubble_sort
from sprint3.k_merge_sort import merge, merge_sort
from sprint3.l_two_bicycles import (
    bisect,
    left_binary_search,
    left_binary_search_rec,
)
from sprint3.m_golden_mean import median_two
from sprint3.n_flowerbeds import union
from sprint3.o_index_difference import min_diff_by_index
from sprint3.p_partial_sort import count_max_blocks


def test_a():
    assert list(bracket_gen(3)) == [
        '((()))',
        '(()())',
        '(())()',
        '()(())',
        '()()()',
    ]

    for n in range(11):
        brackets = list(bracket_gen(n))
        assert brackets == sorted(brackets)
        assert len(brackets) == len(set(brackets))


@pytest.mark.parametrize('func', (phone_combinations, phone_combinations_rec))
def test_b(func):
    assert ' '.join(func('23')) == 'ad ae af bd be bf cd ce cf'
    assert ' '.join(func('92')) == 'wa wb wc xa xb xc ya yb yc za zb zc'


def test_c():
    assert is_subsequence('abc', 'ahbgdcu')
    assert not is_subsequence('abcp', 'ahpc')
    assert is_subsequence('abc', 'xxxxxaxxxxbxxxxcxxx')
    assert not is_subsequence('abc', 'aaaabbb')
    assert not is_subsequence('abcd', 'abcp')


def test_d():
    assert count_happy([1, 2], [2, 1, 3]) == 2
    assert count_happy([2, 1, 3], [1, 1]) == 1
    assert count_happy([1, 1, 1, 5, 7], [1, 1, 2, 3, 3, 3, 6]) == 4


@pytest.mark.parametrize('func', (count_houses, count_houses_acc))
@pytest.mark.parametrize(
    'houses, budget, expected',
    (
        ([999, 999, 999], 300, 0),
        ([350, 999, 200], 1000, 2),
        ([350, 999, 200], 2000, 3),
    ),
)
def test_e(func, houses, budget, expected):
    assert func(houses, budget) == expected


def test_f():
    assert max_perimeter([6, 3, 3, 2]) == 8
    assert max_perimeter([5, 3, 7, 2, 8, 3]) == 20


def test_g():
    assert list(counting_sort([0, 2, 1, 2, 0, 0, 1])) == [0, 0, 0, 1, 1, 2, 2]


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            ['15', '56', '2'],
            '56215',
        ),
        (
            ['1', '783', '2'],
            '78321',
        ),
        (
            ['2', '4', '5', '2', '10'],
            '542210',
        ),
        (
            ['9', '10', '1', '1', '1', '6'],
            '9611110',
        ),
        (
            ['8', '89', '87'],
            '89887',
        ),
    ),
)
def test_h(test_input, expected):
    assert largest_number(test_input) == expected


def test_i():
    assert top_k_schools([1, 2, 3, 1, 2, 3, 4], 3) == [1, 2, 3]
    assert top_k_schools([3, 2, 1, 3, 1, 2, 5, 4], 4) == [1, 2, 3, 4]
    assert top_k_schools([2, 1], 1) == [1]


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [4, 3, 9, 2, 1],
            [
                '3 4 2 1 9',
                '3 2 1 4 9',
                '2 1 3 4 9',
                '1 2 3 4 9',
            ],
        ),
        (
            [1, 2, 3, 4, 5],
            [
                '1 2 3 4 5',
            ],
        ),
    ),
)
def test_j(test_input, expected, capsys):
    run_bubble_sort(test_input)
    assert capsys.readouterr().out.strip().split('\n') == expected


def test_k():
    a = []
    merge_sort(a, 0, len(a))
    assert a == []
    a = [1]
    merge_sort(a, 0, len(a))
    assert a == [1]
    a = [1, 1, 1]
    merge_sort(a, 0, len(a))
    assert a == [1, 1, 1]
    a = [0, 1, 2, 3, 4, 5]
    merge_sort(a, 0, len(a))
    assert a == [0, 1, 2, 3, 4, 5]
    a = [5, 2, 1, 0, 3, 4]
    merge_sort(a, 0, len(a))
    assert a == [0, 1, 2, 3, 4, 5]
    a = [5, 2, 3, 1, 0, 3, 4, 0]
    merge_sort(a, 0, len(a))
    assert a == [0, 0, 1, 2, 3, 3, 4, 5]

    a = [1, 4, 9, 2, 10, 11]
    assert merge(a, 0, 3, 6) == [1, 2, 4, 9, 10, 11]
    a = [1, 4, 2, 10, 1, 2]
    merge_sort(a, 0, 6)
    assert a == [1, 1, 2, 2, 4, 10]


@pytest.mark.parametrize(
    'func', (bisect, left_binary_search, left_binary_search_rec)
)
@pytest.mark.parametrize(
    'a, k, expected',
    (
        ([], 1, -1),
        ([0], 1, -1),
        ([1], 1, 1),
        ([1, 2, 4, 4, 6, 8], 3, 3),
        ([1, 2, 4, 4, 6, 8], 6, 5),
        ([0, 1, 1, 1], 1, 2),
        ([0, 1, 2, 2, 2, 3, 4], 2, 3),
        ([0, 1, 2], 3, -1),
    ),
)
def test_l(func, a, k, expected):
    assert func(a, k) == expected


@pytest.mark.parametrize(
    'a, b, expected',
    (
        ([1, 3], [2], 2),
        ([1, 3], [2, 2, 2, 2, 2], 2),
        ([1, 2], [3], 2),
        ([2], [2, 2], 2),
        ([2], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([1, 4], [2, 3], 2.5),
        ([1, 3, 5], [2, 4], 3),
        ([1, 2, 3, 4, 5, 6], [10], 4),
        ([1, 2, 3, 4, 5, 10], [6], 4),
        ([1, 1, 2, 5, 6, 7], [3, 4, 4, 5, 9, 9, 9, 10, 11, 12], 5.5),
        ([1, 1], [3, 3], 2),
    ),
)
def test_m(a, b, expected):
    result = median_two(a, b)
    assert result == expected
    assert type(result) is type(expected)


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [[7, 8], [7, 8], [2, 3], [6, 10]],
            [[2, 3], [6, 10]],
        ),
        (
            [[2, 3], [5, 6], [3, 4], [3, 4]],
            [[2, 4], [5, 6]],
        ),
        (
            [[1, 3], [3, 5], [4, 6], [5, 6], [2, 4], [7, 10]],
            [[1, 6], [7, 10]],
        ),
        (
            [[7, 8], [6, 7], [1, 3], [1, 4], [2, 5]],
            [[1, 5], [6, 8]],
        ),
    ),
)
def test_n(test_input, expected):
    assert list(union(test_input)) == expected


@pytest.mark.parametrize(
    'nums, index, expected',
    (
        ([2, 3, 4], 2, 1),
        ([1, 3, 1], 1, 0),
        ([1, 3, 5], 3, 4),
        ([7, 2, 7, 3], 4, 4),
        ([9, 1, 10, 3, 4, 6, 2, 7], 6, 2),
    ),
)
def test_o(nums, index, expected):
    assert min_diff_by_index(nums, index) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([0, 1, 3, 2], 3),
        ([3, 6, 7, 4, 1, 5, 0, 2], 1),
        ([1, 0, 2, 3, 4], 4),
    ),
)
def test_p(test_input, expected):
    assert count_max_blocks(test_input) == expected


@pytest.mark.parametrize(
    'test_input, target, expected',
    (
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5, 6),
        ([5, 1], 1, 1),
        ([], 1, -1),
        ([0], 1, -1),
        ([1], 1, 0),
    ),
)
def test_final_search_in_broken_list(test_input, target, expected):
    assert broken_search(test_input, target) == expected


def test_final_search_in_broken_list_random():
    n = 10
    lists = [list(islice(cycle(range(1, 1 + n)), i, i + n)) for i in range(n)]
    for a in lists:
        for i, value in enumerate(a):
            assert broken_search(a, value) == i


@pytest.mark.parametrize(
    'test_input',
    (
        [],
        [1],
        [1, 1],
        [1, 2],
        [2, 1],
        [5, 1, 3, 4, 2],
        [1, 3, 1, 4, 0],
        [5, 1, 1, 2, 4, 2, 6, 0, 0],
    ),
)
def test_quicksort(test_input):
    expected = sorted(test_input)
    quicksort(test_input)
    assert test_input == expected


def test_quicksort_random():
    random.seed(1)
    for _ in range(1000):
        a = random.choices(range(10), k=50)
        expected = sorted(a)
        quicksort(a)
        assert a == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [
                '5',
                'alla 4 100',
                'gena 6 1000',
                'gosha 2 90',
                'rita 2 90',
                'timofey 4 80',
            ],
            [
                'gena',
                'timofey',
                'alla',
                'gosha',
                'rita',
            ],
        ),
        (
            [
                '5',
                'alla 0 0',
                'gena 0 0',
                'gosha 0 0',
                'rita 0 0',
                'timofey 0 0',
            ],
            [
                'alla',
                'gena',
                'gosha',
                'rita',
                'timofey',
            ],
        ),
    ),
)
def test_final_efficient_quicksort(test_input, expected, monkeypatch, capsys):
    inputs = StringIO('\n'.join(test_input))
    monkeypatch.setattr('sys.stdin', inputs)
    main()
    assert capsys.readouterr().out.strip().split('\n') == expected
