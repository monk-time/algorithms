from io import StringIO

import pytest

from bonus1 import b_crash_me, c_prefix_hashes
from bonus1.a_polynomial_hash import polynomial_hash


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
