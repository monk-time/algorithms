import pytest

from sprint2 import (
    b_todo,
    c_tedious_work,
    d_caring_mother,
    e_reversed,
    f_stack_max,
    final_deque,
    i_limited_queue,
    j_list_queue,
)
from sprint2.a_monitoring import transpose
from sprint2.h_bracket_sequence import is_correct_bracket_seq
from sprint2.k_rec_fibonacci import fib
from sprint2.l_mod_fibonacci import fib_mod


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


@pytest.mark.parametrize(
    'commands, expected',
    (
        (
            (
                'get_max',
                'push 7',
                'pop',
                'push -2',
                'push -1',
                'pop',
                'get_max',
                'get_max',
            ),
            [
                'None',
                '-2',
                '-2',
            ],
        ),
        (
            (
                'pop',
                'push 1',
                'push 1',
                'push 1',
                'get_max',
                'pop',
                'get_max',
                'get_max',
                'pop',
                'pop',
                'get_max',
                'pop',
            ),
            [
                'error',
                '1',
                '1',
                '1',
                'None',
                'error',
            ],
        ),
        (
            (
                'pop',
                'pop',
                'push 4',
                'push -5',
                'push 7',
                'pop',
                'pop',
                'get_max',
            ),
            [
                'error',
                'error',
                '4',
            ],
        ),
        (
            (
                'get_max',
                'push -6',
                'pop',
                'pop',
                'get_max',
                'push 2',
                'get_max',
                'pop',
                'push -2',
            ),
            [
                'None',
                'error',
                'None',
                '2',
            ],
        ),
    ),
)
def test_f(commands, expected, capsys):
    stack = f_stack_max.StackMax()
    for command in commands:
        f_stack_max.execute(command, stack)
    assert capsys.readouterr().out.split() == expected


@pytest.mark.parametrize(
    'test_input, expected',
    (
        ('()', True),
        ('(())', True),
        ('{[()]}', True),
        ('()()()', True),
        ('()[]{}', True),
        ('([]){[]}((({})))', True),
        ('(', False),
        (')', False),
        ('()[', False),
        ('[{}(]', False),
        (']()]', False),
    ),
)
def test_h(test_input, expected):
    assert is_correct_bracket_seq(test_input) == expected


@pytest.mark.parametrize(
    'max_size, commands, expected',
    (
        (
            2,
            (
                'peek',
                'push 5',
                'push 2',
                'peek',
                'size',
                'size',
                'push 1',
                'size',
            ),
            [
                'None',
                '5',
                '2',
                '2',
                'error',
                '2',
            ],
        ),
        (
            1,
            (
                'push 3',
                'size',
                'push 4',
                'size',
                'push 5',
                'pop',
                'push 6',
                'pop',
            ),
            [
                '1',
                'error',
                '1',
                'error',
                '3',
                '6',
            ],
        ),
    ),
)
def test_i(max_size, commands, expected, capsys):
    queue = i_limited_queue.MyQueueSized(max_size)
    for command in commands:
        i_limited_queue.execute(command, queue)
    assert capsys.readouterr().out.split() == expected


@pytest.mark.parametrize(
    'commands, expected',
    (
        (
            (
                'put -34',
                'put -23',
                'get',
                'size',
                'get',
                'size',
                'get',
                'get',
                'put 80',
                'size',
            ),
            [
                '-34',
                '1',
                '-23',
                '0',
                'error',
                'error',
                '1',
            ],
        ),
    ),
)
def test_j(commands, expected, capsys):
    queue = j_list_queue.ListQueue()
    for command in commands:
        j_list_queue.execute(command, queue)
    assert capsys.readouterr().out.split() == expected


def test_k():
    assert fib(0) == 1
    assert fib(1) == 1
    assert fib(2) == 2
    assert fib(3) == 3
    assert fib(10) == 89


def test_l():
    assert fib_mod(0, 1) == 1
    assert fib_mod(1, 1) == 1
    assert fib_mod(2, 1) == 2
    assert fib_mod(3, 1) == 3
    assert fib_mod(10, 2) == 89
    assert fib_mod(10, 4) == 89
    assert fib_mod(100, 5) == 84101
    assert fib_mod(10**6, 8) == 26937501


@pytest.mark.parametrize(
    'max_size, commands, expected',
    (
        (
            4,
            (
                'push_front 861',
                'push_front -819',
                'pop_back',
                'pop_back',
            ),
            [
                '861',
                '-819',
            ],
        ),
        (
            4,
            (
                'pop_front',
                'pop_back',
                'push_back 2',
                'push_front 1',
                'push_back 3',
                'push_front 0',
                'pop_back',
                'pop_front',
                'push_back 4',
                'push_front -1',
                'pop_front',
                'pop_front',
                'pop_front',
                'pop_front',
                'pop_front',
            ),
            [
                'error',
                'error',
                '3',
                '0',
                '-1',
                '1',
                '2',
                '4',
                'error',
            ]
        )
    ),
)
def test_deque(max_size, commands, expected, capsys):
    queue = final_deque.Deque(max_size)
    for command in commands:
        final_deque.execute(command, queue)
    assert capsys.readouterr().out.split() == expected
