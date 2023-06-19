from io import StringIO

import pytest

from bonus1 import b_crash_me, c_prefix_hashes
from bonus1.a_polynomial_hash import polynomial_hash
from bonus1.d_workshops import unique
from bonus1.e_substrings import max_substring_with_no_repeatitions
from bonus1.f_anagram_grouping import anagram_groups
from bonus1.g_competition import longest_balanced
from bonus1.h_weird_comparison import weird_compare


@pytest.mark.parametrize(
    'a, m, s, expected',
    (
        (123, 100003, 'a', 97),
        (123, 100003, 'hash', 6080),
        (123, 100003, 'HaSH', 56156),
    ),
)
def test_a(a, m, s, expected):
    assert polynomial_hash(a, m, s) == expected


def test_b():
    s1, s2 = b_crash_me.find_collision()
    assert b_crash_me.polynomial_hash(s1) == b_crash_me.polynomial_hash(s2)


def test_prefix_hashes():
    a, m, s = 1000, 1000009, 'abcdefgh'
    prefixes = c_prefix_hashes.prefix_hashes(a, m, s)
    for i, h in enumerate(prefixes):
        assert h == polynomial_hash(a, m, s[: i + 1])


def test_substring_hash():
    a, m, s = 1000, 1000009, 'abcdefgh'
    prefixes = c_prefix_hashes.prefix_hashes(a, m, s)
    for i in range(len(s)):
        for j in range(i, len(s)):
            test_value = c_prefix_hashes.substring_hash(a, m, prefixes, i, j)
            expected = polynomial_hash(a, m, s[i : j + 1])
            assert test_value == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [
                '1000',
                '1000009',
                'abcdefgh',
                '7',
                '1 1',
                '1 5',
                '2 3',
                '3 4',
                '4 4',
                '1 8',
                '5 8',
            ],
            [
                '97',
                '225076',
                '98099',
                '99100',
                '100',
                '436420',
                '193195',
            ],
        ),
        (
            [
                '100',
                '10',
                'a',
                '1',
                '1 1',
            ],
            [
                '7',
            ],
        ),
    ),
)
def test_c(test_input, expected, monkeypatch, capsys):
    inputs = StringIO('\n'.join(test_input))
    monkeypatch.setattr('sys.stdin', inputs)
    c_prefix_hashes.main()
    assert capsys.readouterr().out.strip().split('\n') == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [
                'вышивание крестиком',
                'рисование мелками на парте',
                'настольный керлинг',
                'настольный керлинг',
                'кухня африканского племени ужасмай',
                'тяжелая атлетика',
                'таракановедение',
                'таракановедение',
            ],
            [
                'вышивание крестиком',
                'рисование мелками на парте',
                'настольный керлинг',
                'кухня африканского племени ужасмай',
                'тяжелая атлетика',
                'таракановедение',
            ],
        ),
        ([1, 4, 2, 5, 4, 2, 3, 1, 2], [1, 4, 2, 5, 3]),
    ),
)
def test_d(test_input, expected):
    assert unique(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('awe', 3),
    ),
)
def test_e(test_input, expected):
    assert max_substring_with_no_repeatitions(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (['tan', 'eat', 'tea', 'ate', 'nat', 'bat'], [[0, 4], [1, 2, 3], [5]]),
        (['tan', 'nat', 'tantan'], [[0, 1], [2]]),
    ),
)
def test_f(test_input, expected):
    assert anagram_groups(test_input) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('0 1', 2),
        ('0 1 0', 2),
        ('0 0 1 0 1 1 1 0 0 0', 8),
        ('1 0 0 0 0 1 0 1', 4),
        ('1 1', 0),
        ('1 1 1 1', 0),
        ('0 0 1 0 0 0 1 0 0 1', 4),
        ('0 0 1 0 0 1 1 1 1 1 0 0 0 0 0 1', 14),
        ('0 0 1 0 0 1 1 1 1 1 0 0', 12),
        ('1 0 0 0 1 1', 6),
        ('0 1 0 0 0 1 1 1', 8),
        ('1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0', 16),
    ),
)
def test_g(test_input, expected):
    assert longest_balanced(test_input.split()) == expected


@pytest.mark.parametrize(
    's, t, expected',
    (
        ('mxyskaoghi', 'qodfrgmslc', True),
        ('agg', 'xdd', True),
        ('agg', 'xda', False),
        ('abacaba', 'xhxixhx', True),
        ('abc', 'aaa', False),
        ('agg', 'pap', False),
        ('aabba', 'ccddc', True),
        ('aabba', 'ccddd', False),
    ),
)
def test_h(s, t, expected):
    assert weird_compare(s, t) == expected
