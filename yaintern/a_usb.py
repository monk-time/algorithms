def min_price(
    port_count: int, gadget_count: int, price_c2: int, price_c5: int
) -> int:
    req_ports = gadget_count - port_count
    if req_ports <= 0:
        return 0
    req_sets_of_four, req_rest = divmod(req_ports, 4)
    return req_sets_of_four * min(4 * price_c2, price_c5) + min(
        req_rest * price_c2, price_c5
    )


if __name__ == '__main__':
    port_count, gadget_count, price_c2, price_c5 = (
        int(input()) for _ in range(4)
    )
    print(min_price(port_count, gadget_count, price_c2, price_c5))
