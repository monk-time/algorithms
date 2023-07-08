import pytest

from shbr4.a_groups_and_rooms import max_groups
from shbr4.b_guests import find_dates
from shbr4.c_socks import thickness
from shbr4.d_subtree_size import create_directed_tree, subtree_sizes
from shbr4.e_filepath import find_path


@pytest.mark.parametrize(
    'groups, rooms, expected',
    (
        ([3, 1, 2], [1, 1], 1),
        ([1, 2], [3, 2, 1], 2),
        ([2, 2, 2], [0, 0], 0),
        ([2, 2, 2], [2, 2, 2], 3),
        ([2, 2, 2], [4, 4, 4, 4], 3),
        ([2, 2, 2], [4, 4], 2),
    ),
)
def test_a(groups, rooms, expected):
    assert max_groups(groups, rooms) == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ([[1, 2], [2, 4], [3, 5]], [[1, 2], [3, 4], [5, 5]]),
        ([[2, 3], [1, 4], [3, 5]], [[-1, -1], [1, 4], [5, 5]]),
    ),
)
def test_b(test_input, expected):
    assert find_dates(test_input) == expected


@pytest.mark.parametrize(
    'socks, points, expected',
    (
        (
            [
                [6, 11],
                [10, 15],
                [3, 18],
                [1, 19],
                [10, 17],
                [1, 10],
                [6, 16],
                [20, 21],
                [1, 1],
                [12, 21],
                [5, 9],
                [1, 10],
                [5, 10],
                [6, 11],
                [5, 6],
                [7, 11],
                [1, 19],
                [13, 15],
            ],
            [5, 22, 19, 3, 8, 16, 16, 21],
            [8, 0, 3, 5, 11, 6, 6, 2],
        ),
    ),
)
def test_c(socks, points, expected):
    assert thickness(socks, points) == expected


@pytest.mark.parametrize(
    'vertice_count, edges, expected',
    (
        (
            4,
            [[1, 2], [1, 3], [1, 4]],
            [4, 1, 1, 1],
        ),
        (
            7,
            [[1, 2], [1, 3], [1, 4], [5, 1], [5, 6], [5, 7]],
            [7, 1, 1, 1, 3, 1, 1],
        ),
    ),
)
def test_d(vertice_count, edges, expected):
    nodes = create_directed_tree(vertice_count, edges)
    assert subtree_sizes(nodes) == expected


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
    'filetree, filename, expected',
    (
        (sample_filetree, '1.avi', '/emoh/vorodis/onrop/1.avi'),
        (sample_filetree, '2.avi', '/emoh/vorodis/onrop/2.avi'),
        (sample_filetree, 'a.doc', '/emoh/vonavi/a.doc'),
        (sample_filetree, 'b.doc', '/emoh/vonavi/b.doc'),
        (sample_filetree, '.bashrc', '/emoh/vortep/.bashrc'),
        (sample_filetree, 'top.doc', '/top.doc'),
    ),
)
def test_e(filetree, filename, expected):
    assert find_path(filetree, filename) == expected
