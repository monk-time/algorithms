def moving_average(a, k):
    current_sum = sum(a[0:k])
    result = [current_sum / k]
    for i in range(len(a) - k):
        current_sum += a[i + k] - a[i]
        result.append(current_sum / k)
    return result


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(' '.join(map(str, moving_average(a, k))))
