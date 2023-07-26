from collections import deque

def is_valid_move(x, y, h, w):
    return 0 <= x < h and 0 <= y < w

def bfs_with_wall_removal(start, end, map):
    h, w = len(map), len(map[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = deque([(start[0], start[1], False, 1)])  # (x, y, wall_removed, steps)
    visited = set()

    while queue:
        x, y, wall_removed, steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if is_valid_move(new_x, new_y, h, w) and (new_x, new_y, wall_removed) not in visited:
                visited.add((new_x, new_y, wall_removed))

                if map[new_x][new_y] == 0:
                    queue.append((new_x, new_y, wall_removed, steps + 1))
                elif map[new_x][new_y] == 1 and not wall_removed:
                    queue.append((new_x, new_y, True, steps + 1))

    # If the escape pod is unreachable, return -1 or any other appropriate value
    return -1

def solution(map):
    start = (0, 0)
    end = (len(map) - 1, len(map[0]) - 1)
    return bfs_with_wall_removal(start, end, map)


map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]

print(solution(map))