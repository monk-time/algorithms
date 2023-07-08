def max_groups(groups: list[int], rooms: list[int]) -> int:
    groups.sort()
    rooms.sort()
    group_i, room_i = 0, 0
    while group_i < len(groups):
        while room_i < len(rooms) and groups[group_i] > rooms[room_i]:
            room_i += 1
        if room_i >= len(rooms):
            break
        room_i += 1
        group_i += 1
    return group_i


if __name__ == '__main__':
    _ = input()
    groups = [int(s) for s in input().split()]
    _ = input()
    rooms = [int(s) for s in input().split()]
    print(max_groups(groups, rooms))
