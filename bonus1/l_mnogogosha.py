def polynomial_hash(s: str, q: int, m: int) -> int:
    hash_ = 0
    for ch in s:
        ch_num = ord(ch) - ord('a') + 1
        hash_ = (hash_ * q + ch_num) % m
    return hash_


def substrings_k_times(s: str, n: int, k: int) -> list[int]:
    # One hash gives too many collisions. Let's use two hashes!
    m_1, m_2 = 10**9 + 7, 10**9 + 9
    q_1, q_2 = 31, 29
    q_1_big = pow(q_1, n - 1, m_1)
    q_2_big = pow(q_2, n - 1, m_2)
    hash_1 = polynomial_hash(s[:n], q_1, m_1)
    hash_2 = polynomial_hash(s[:n], q_2, m_2)
    counter = {(hash_1, hash_2): [0, 1]}
    for i in range(1, len(s) - n + 1):
        ch_prev = ord(s[i - 1]) - ord('a') + 1
        ch_next = ord(s[i + n - 1]) - ord('a') + 1
        hash_1 = ((hash_1 - ch_prev * q_1_big) * q_1 + ch_next) % m_1
        hash_2 = ((hash_2 - ch_prev * q_2_big) * q_2 + ch_next) % m_2
        if (hash_1, hash_2) not in counter:
            counter[(hash_1, hash_2)] = [i, 1]
        else:
            counter[(hash_1, hash_2)][1] += 1
    return [i for i, count in counter.values() if count >= k]


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(*substrings_k_times(s, n, k))
