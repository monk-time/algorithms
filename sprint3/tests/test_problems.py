import random
from io import StringIO
from itertools import cycle, islice

import pytest

from sprint3.a_bracket_gen import bracket_gen
from sprint3.b_combinations import phone_combinations
from sprint3.c_subsequence import is_subsequence
from sprint3.d_cookies import count_happy
from sprint3.e_houses import count_houses
from sprint3.f_triangle import max_perimeter
from sprint3.final_efficient_quicksort import main, quicksort
from sprint3.final_search_in_broken_list import search_in_shifted
from sprint3.g_wardrobe import count_colors
from sprint3.h_large_number import largest_number
from sprint3.i_conference_fans import top_k_schools
from sprint3.j_bubble import run_bubble_sort
from sprint3.k_merge_sort import merge, merge_sort
from sprint3.l_two_bicycles import (
    bisect,
    left_binary_search_mod,
    left_binary_search_mod2,
)
from sprint3.n_flowerbeds import union


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


def test_b():
    assert ' '.join(phone_combinations('23')) == 'ad ae af bd be bf cd ce cf'
    assert (
        ' '.join(phone_combinations('92'))
        == 'wa wb wc xa xb xc ya yb yc za zb zc'
    )


def test_c():
    assert is_subsequence('abc', 'ahbgdcu')
    assert is_subsequence('abc', 'xxxxxaxxxxbxxxxcxxx')
    assert not is_subsequence('abc', 'aaaabbb')
    assert not is_subsequence('abcd', 'abcp')


def test_d():
    assert count_happy([1, 2], [2, 1, 3]) == 2
    assert count_happy([2, 1, 3], [1, 1]) == 1
    assert count_happy([1, 1, 1, 5, 7], [1, 1, 2, 3, 3, 3, 6]) == 4


def test_e():
    assert count_houses([999, 999, 999], 300) == 0
    assert count_houses([350, 999, 200], 1000) == 2


def test_f():
    assert max_perimeter([6, 3, 3, 2]) == 8
    assert max_perimeter([5, 3, 7, 2, 8, 3]) == 20


def test_g():
    assert list(count_colors([0, 2, 1, 2, 0, 0, 1])) == [0, 0, 0, 1, 1, 2, 2]


def test_h():
    assert largest_number(['15', '56', '2']) == '56215'
    assert largest_number(['1', '783', '2']) == '78321'


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
    'function', (bisect, left_binary_search_mod, left_binary_search_mod2)
)
def test_l(function):
    assert function([], 1) == -1
    assert function([0], 1) == -1
    assert function([1], 1) == 1
    assert function([1, 2, 4, 4, 6, 8], 3) == 3
    assert function([1, 2, 4, 4, 6, 8], 6) == 5
    assert function([0, 1, 1, 1], 1) == 2
    assert function([0, 1, 2, 2, 2, 3, 4], 2) == 3
    assert function([0, 1, 2], 3) == -1


def test_n():
    assert list(union([[7, 8], [7, 8], [2, 3], [6, 10]])) == [
        [2, 3],
        [6, 10],
    ]
    assert list(union([[7, 8], [6, 7], [1, 3], [1, 4], [2, 5]])) == [
        [1, 5],
        [6, 8],
    ]


def test_final_search_in_broken_list():
    assert search_in_shifted([19, 21, 100, 101, 1, 4, 5, 7, 12], 5) == 6
    assert search_in_shifted([], 1) == -1
    assert search_in_shifted([0], 1) == -1
    assert search_in_shifted([1], 1) == 0
    n = 10
    lists = [list(islice(cycle(range(1, 1 + n)), i, i + n)) for i in range(n)]
    for a in lists:
        for i, value in enumerate(a):
            assert search_in_shifted(a, value) == i


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
    ),
)
def test_final_efficient_quicksort(test_input, expected, monkeypatch, capsys):
    inputs = StringIO('\n'.join(test_input))
    monkeypatch.setattr('sys.stdin', inputs)
    main()
    assert capsys.readouterr().out.strip().split('\n') == expected
