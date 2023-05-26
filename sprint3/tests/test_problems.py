import pytest

from sprint3.a_bracket_gen import bracket_gen
from sprint3.b_combinations import phone_combinations
from sprint3.c_subsequence import is_subsequence
from sprint3.d_cookies import count_happy
from sprint3.e_houses import count_houses
from sprint3.f_triangle import max_perimeter
from sprint3.g_wardrobe import count_colors
from sprint3.h_large_number import largest_number
from sprint3.i_conference_fans import top_k_schools
from sprint3.j_bubble import run_bubble_sort
from sprint3.k_merge_sort import merge_sort
from sprint3.l_two_bicycles import left_binary_search_mod


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


def test_l():
    a = [1, 2, 4, 4, 6, 8]
    assert left_binary_search_mod(a, k=3, left=0, right=len(a)) == 3
    assert left_binary_search_mod(a, k=6, left=0, right=len(a)) == 5
    a = [0, 1, 1, 1]
    assert left_binary_search_mod(a, k=1, left=0, right=len(a)) == 2
    a = [0, 1, 1, 1]
    assert left_binary_search_mod(a, k=1, left=1, right=len(a)) == 2
    a = [0, 1, 1, 1]
    assert left_binary_search_mod(a, k=1, left=2, right=len(a)) == 3
    a = [0, 1, 1, 1]
    assert left_binary_search_mod(a, k=1, left=0, right=1) == -1
    a = [0, 1, 1, 1]
    assert left_binary_search_mod(a, k=1, left=0, right=2) == 2
    a = [0, 1, 2, 2, 2, 3, 4]
    assert left_binary_search_mod(a, k=2, left=0, right=len(a)) == 3
    a = [0, 1, 2]
    assert left_binary_search_mod(a, k=3, left=0, right=len(a)) == -1
