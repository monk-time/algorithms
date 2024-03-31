from io import StringIO

import pytest

from shbr3.a_count_positive import main
from shbr3.b_boomers_and_zoomers import count_invitations
from shbr3.c_festive_lights import count_max_lights, make_x_same_lights
from shbr3.d_cows_in_stalls import can_fit_at_x_distance, max_min_distance
from shbr3.e_brewing_potions import max_sum_quality


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (
            [
                '5',
                '2 -1 2 -2 3',
                '4',
                '1 1',
                '1 3',
                '2 4',
                '1 5',
            ],
            ['1', '2', '1', '3'],
        ),
    ),
)
def test_a(test_input, expected, monkeypatch, capsys):
    inputs = StringIO('\n'.join(test_input))
    monkeypatch.setattr('sys.stdin', inputs)
    main()
    assert capsys.readouterr().out.strip().split('\n') == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([16, 16], 2),
        ([17, 16, 18], 2),
        ([120, 25, 30, 100, 105], 4),
        ([16, 16, 16], 6),
        ([16, 16, 16, 16], 12),
        ([16, 17, 17], 4),
        ([16, 16, 17, 17, 17], 14),
        ([7, 7, 28], 0),
    ),
)
def test_b(test_input, expected):
    assert count_invitations(test_input) == expected


@pytest.mark.parametrize(
    'sorted_counts, lights_len, x, expected',
    (
        ((50, 30, 10, 6, 2), 5, 2, (5,)),
        ((50, 30, 10, 6, 2), 5, 10, (5,)),
        ((50, 30, 10, 6, 2), 5, 12, (4, 1)),
        ((50, 30, 10, 6, 2), 5, 15, (3, 2)),
        ((50, 30, 10, 6, 2), 5, 16, None),
    ),
)
def test_make_x_same_lights(sorted_counts, lights_len, x, expected):
    assert make_x_same_lights(sorted_counts, lights_len, x) == expected


@pytest.mark.parametrize(
    'n, a, max_count, max_lights',
    (
        (3, (3, 3, 2, 1), 2, (1, 2, 3)),
        (6, (15, 10, 8, 7, 6, 5, 1), 6, (1, 1, 2, 3, 4, 5)),
        (5, (50, 30, 10, 6, 2), 15, (1, 1, 1, 2, 2)),
    ),
)
def test_c(n, a, max_count, max_lights):
    assert count_max_lights(a, n) == (max_count, max_lights)


@pytest.mark.parametrize(
    'a, total_count, x, expected',
    (
        ([2, 5, 7, 11, 15, 20], 6, 2, True),
        ([2, 5, 7, 11, 15, 20], 6, 3, False),
        ([2, 5, 7, 11, 15, 20], 3, 9, True),
        ([2, 5, 7, 11, 15, 20], 3, 10, False),
    ),
)
def test_can_fit_at_x_distance(a, total_count, x, expected):
    assert can_fit_at_x_distance(a, total_count, x) == expected


@pytest.mark.parametrize(
    'a, k, expected',
    (
        ([2, 5, 7, 11, 15, 20], 2, 18),
        ([2, 5, 7, 11, 15, 20], 3, 9),
        ([2, 5, 7, 11, 15, 20], 4, 5),
        ([2, 5, 7, 11, 15, 20], 5, 4),
        ([2, 5, 7, 11, 15, 20], 6, 2),
    ),
)
def test_d(a, k, expected):
    assert max_min_distance(a, k) == expected


@pytest.mark.parametrize(
    'a, k, expected',
    (
        ([-2, 3, -5, 5, 1], 5, 26),
        ([-1, 1], 2, 1),
        ([101, 100, 3, 2, 1], 1, 201),
        ([101, 100, 3, 2, 1], 2, 305),
        ([101, 100, 3, 2, 1], 3, 408),
        ([101, 100, 3, 2, 1], 4, 511),
        ([101, 100, 3, 2, 1], 5, 613),
        ([101, 100, 3, 2, 1], 6, 715),
        ([101, 100, 3, 2, 1], 7, 816),
        ([101, 100, 3, 2, 1], 8, 917),
        ([101, 100, 3, 2, 1], 9, 1017),
        ([101, 100, 3, 2, 1], 10, 1022),
        ([101, 100, 3, 2, 1], 11, 1026),
        ([101, 100, 3, 2, 1], 12, 1029),
        ([101, 100, 3, 2, 1], 13, 1032),
        ([101, 100, 3, 2, 1], 14, 1034),
        ([101, 100, 3, 2, 1], 15, 1035),
    ),
)
def test_e(a, k, expected):
    assert max_sum_quality(a, k) == expected
