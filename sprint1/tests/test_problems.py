from sprint1.a_function_values import func
from sprint1.b_even_odd import check_parity
from sprint1.c_neighbors import neighbors, parse_matrix
from sprint1.d_weather import calc_chaos
from sprint1.e_longest_word import find_longest_word
from sprint1.f_palindrome import is_palindrome
from sprint1.final_nearest_zero import nearest_zeroes
from sprint1.final_sleight_of_hand import max_score
from sprint1.g_working_from_home import to_binary
from sprint1.h_binary import binary_sum
from sprint1.i_power_of_four import is_power_of_four
from sprint1.j_factorization import factorization
from sprint1.k_list_form import special_sum
from sprint1.l_extra_letter import extra_letter


def test_a():
    assert func(-8, -5, -2, 7) == -183
    assert func(8, 2, 9, -10) == 40


def test_b():
    assert check_parity(1, 2, -3) == 'FAIL'
    assert check_parity(7, 11, 7) == 'WIN'
    assert check_parity(6, -2, 0) == 'WIN'


def test_c():
    matrix = parse_matrix(
        [
            '1 2 3',
            '0 2 6',
            '7 4 1',
            '2 7 0',
        ]
    )
    assert neighbors(matrix, 3, 0) == [7, 7]
    assert neighbors(matrix, 0, 0) == [0, 2]


def test_d():
    assert calc_chaos([-1, -10, -8, 0, 2, 0, 5]) == 3
    assert calc_chaos([1, 2, 5, 4, 8]) == 2


def test_e():
    assert find_longest_word('i love segment tree') == 'segment'
    assert find_longest_word('frog jumps from river') == 'jumps'


def test_f():
    assert is_palindrome('A man, a plan, a canal: Panama')
    assert not is_palindrome('A man')


def test_g():
    assert to_binary(0) == '0'
    assert to_binary(5) == '101'
    assert to_binary(16) == '10000'


def test_h():
    assert binary_sum('1010', '1011') == '10101'
    assert binary_sum('1', '1000') == '1001'
    assert binary_sum('1', '1') == '10'
    assert binary_sum('1', '0') == '1'
    assert binary_sum('0', '0') == '0'


def test_i():
    assert not is_power_of_four(15)
    assert not is_power_of_four(257)
    assert is_power_of_four(4)
    assert is_power_of_four(16)
    assert is_power_of_four(256)


def test_j():
    assert list(factorization(8)) == [2, 2, 2]
    assert list(factorization(2 * 3 * 3 * 5 * 11)) == [2, 3, 3, 5, 11]
    assert list(factorization(1)) == [1]


def test_k():
    assert special_sum([1, 2, 0, 0], 34) == [1, 2, 3, 4]
    assert special_sum([9, 5], 17) == [1, 1, 2]


def test_l():
    assert extra_letter('abcd', 'abcde') == 'e'
    assert extra_letter('abc', 'abcb') == 'b'


def test_nearest_zeroes():
    assert nearest_zeroes([0, 1, 4, 9, 0]) == [0, 1, 2, 1, 0]
    assert nearest_zeroes([0, 1, 2, 3, 4, 0]) == [0, 1, 2, 2, 1, 0]
    assert nearest_zeroes([1, 2, 3, 0, 4, 5, 0, 6]) == [3, 2, 1, 0, 1, 1, 0, 1]
    assert nearest_zeroes([1, 0, 0, 2]) == [1, 0, 0, 1]
    assert nearest_zeroes([1, 0, 0, 2, 3]) == [1, 0, 0, 1, 2]


def test_max_score():
    assert max_score(['1231', '2..2', '2..2', '2..2'], 2) == 2
    assert max_score(['1111', '9999', '1111', '9911'], 4) == 1
    assert max_score(['1111', '1111', '1111', '1111'], 4) == 0
