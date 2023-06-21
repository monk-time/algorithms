import pytest

from bonus2 import (
    a_lamps,
    b_balanced_tree,
    c_anagram_tree,
    d_tree_twins,
    e_search_tree,
    f_max_depth,
    g_max_path,
    h_num_paths,
    i_different_search_trees,
    j_add_node,
    k_show_range,
    l_sieve_down,
    m_sieve_up,
    n_tree_partition,
)


def test_a():
    node1 = a_lamps.Node(1)
    node2 = a_lamps.Node(-5)
    node3 = a_lamps.Node(3, node1, node2)
    node4 = a_lamps.Node(2, node3, None)
    assert a_lamps.solution(node4) == 3


def test_b():
    node1 = b_balanced_tree.Node(1)
    node2 = b_balanced_tree.Node(-5)
    node3 = b_balanced_tree.Node(3, node1, node2)
    node4 = b_balanced_tree.Node(10)
    node5 = b_balanced_tree.Node(2, node3, node4)
    assert b_balanced_tree.solution(node5)


def test_c():
    node1 = c_anagram_tree.Node(3, None, None)
    node2 = c_anagram_tree.Node(4, None, None)
    node3 = c_anagram_tree.Node(4, None, None)
    node4 = c_anagram_tree.Node(3, None, None)
    node5 = c_anagram_tree.Node(2, node1, node2)
    node6 = c_anagram_tree.Node(2, node3, node4)
    node7 = c_anagram_tree.Node(1, node5, node6)
    assert c_anagram_tree.solution(node7)


def test_d():
    node1 = d_tree_twins.Node(1, None, None)
    node2 = d_tree_twins.Node(2, None, None)
    node3 = d_tree_twins.Node(3, node1, node2)
    node4 = d_tree_twins.Node(1, None, None)
    node5 = d_tree_twins.Node(2, None, None)
    node6 = d_tree_twins.Node(3, node4, node5)
    assert d_tree_twins.solution(node3, node6)


def test_e():
    node1 = e_search_tree.Node(1, None, None)
    node2 = e_search_tree.Node(4, None, None)
    node3 = e_search_tree.Node(3, node1, node2)
    node4 = e_search_tree.Node(8, None, None)
    node5 = e_search_tree.Node(5, node3, node4)
    assert e_search_tree.solution(node5)
    node2.value = 5
    assert not e_search_tree.solution(node5)


def test_f():
    node1 = f_max_depth.Node(1, None, None)
    node2 = f_max_depth.Node(4, None, None)
    node3 = f_max_depth.Node(3, node1, node2)
    node4 = f_max_depth.Node(8, None, None)
    node5 = f_max_depth.Node(5, node3, node4)
    assert f_max_depth.solution(node5) == 3


def test_g():
    node1 = g_max_path.Node(5, None, None)
    node2 = g_max_path.Node(1, None, None)
    node3 = g_max_path.Node(-3, node2, node1)
    node4 = g_max_path.Node(2, None, None)
    node5 = g_max_path.Node(2, node4, node3)
    assert g_max_path.solution(node5) == 6


def test_h():
    node1 = h_num_paths.Node(2, None, None)
    node2 = h_num_paths.Node(1, None, None)
    node3 = h_num_paths.Node(3, node1, node2)
    node4 = h_num_paths.Node(2, None, None)
    node5 = h_num_paths.Node(1, node4, node3)
    assert h_num_paths.solution(node5) == 275


@pytest.mark.parametrize(
    'test_input, expected',
    (
        (2, 2),
        (3, 5),
        (4, 14),
    ),
)
def test_i(test_input, expected):
    assert i_different_search_trees.count_distinct(test_input) == expected


def test_j():
    node1 = j_add_node.Node(None, None, 7)
    node2 = j_add_node.Node(node1, None, 8)
    node3 = j_add_node.Node(None, node2, 7)
    new_head = j_add_node.insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6  # type: ignore


def test_k(capsys):
    node1 = k_show_range.Node(None, None, 2)
    node2 = k_show_range.Node(None, node1, 1)
    node3 = k_show_range.Node(None, None, 8)
    node4 = k_show_range.Node(None, node3, 8)
    node5 = k_show_range.Node(node4, None, 9)
    node6 = k_show_range.Node(node5, None, 10)
    node7 = k_show_range.Node(node2, node6, 5)
    k_show_range.print_range(node7, 2, 8)
    assert capsys.readouterr().out.strip().split('\n') == ['2', '5', '8', '8']


def test_l():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert l_sieve_down.sift_down(sample, 2) == 5


def test_m():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert m_sieve_up.sift_up(sample, 5) == 1


def test_n():
    node1 = n_tree_partition.Node(None, None, 3, 1)
    node2 = n_tree_partition.Node(None, node1, 2, 2)
    node3 = n_tree_partition.Node(None, None, 8, 1)
    node4 = n_tree_partition.Node(None, None, 11, 1)
    node5 = n_tree_partition.Node(node3, node4, 10, 3)
    node6 = n_tree_partition.Node(node2, node5, 5, 6)
    left, right = n_tree_partition.split(node6, 4)
    assert left.size == 4
    assert right.size == 2
