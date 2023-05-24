from sprint3.a_bracket_gen import bracket_gen
from sprint3.b_combinations import phone_combinations
from sprint3.c_subsequence import is_subsequence
from sprint3.d_cookies import count_happy


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
