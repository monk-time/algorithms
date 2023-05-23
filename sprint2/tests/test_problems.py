import pytest

from sprint2 import b_todo, c_tedious_work, d_caring_mother, e_reversed
from sprint2.a_monitoring import transpose


def test_a():
    assert transpose(
        [
            [1, 2, 3],
            [0, 2, 6],
            [7, 4, 1],
            [2, 7, 0],
        ]
    ) == [
        [1, 0, 7, 2],
        [2, 2, 4, 7],
        [3, 6, 1, 0],
    ]


def test_b(capsys):
    node3 = b_todo.Node('node3', None)
    node2 = b_todo.Node('node2', node3)
    node1 = b_todo.Node('node1', node2)
    node0 = b_todo.Node('node0', node1)
    b_todo.solution(node0)
    captured = capsys.readouterr()
    stdout = captured.out
    assert stdout == 'node0\nnode1\nnode2\nnode3\n'


def test_c():
    node3 = c_tedious_work.Node('node3', None)
    node2 = c_tedious_work.Node('node2', node3)
    node1 = c_tedious_work.Node('node1', node2)
    node0 = c_tedious_work.Node('node0', node1)
    new_head = c_tedious_work.solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None


@pytest.mark.parametrize(
    'func', (d_caring_mother.solution, d_caring_mother.solution_iter)
)
def test_d(func):
    node3 = d_caring_mother.Node('node3', None)
    node2 = d_caring_mother.Node('node2', node3)
    node1 = d_caring_mother.Node('node1', node2)
    node0 = d_caring_mother.Node('node0', node1)
    assert func(node0, 'node0') == 0
    assert func(node0, 'node1') == 1
    assert func(node0, 'node2') == 2
    assert func(node0, 'node3') == 3
    assert func(node0, 'node4') == -1


def test_e():
    node3 = e_reversed.DoubleConnectedNode('node3')
    node2 = e_reversed.DoubleConnectedNode('node2')
    node1 = e_reversed.DoubleConnectedNode('node1')
    node0 = e_reversed.DoubleConnectedNode('node0')

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2

    new_head = e_reversed.solution(node0)

    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1
