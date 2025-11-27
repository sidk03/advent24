def read_file(file_name: str) -> list[list[str]]:
    grid = []
    with open(file_name) as f:
        for line in f:
            grid.append(list(line.strip()))
    return grid


def run_trace(grid: list[list[str]]) -> int:
    turn = {"^": ">", ">": "v", "v": "<", "<": "^"}
    directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    visited = set()
    m, n = len(grid), len(grid[0])

    for r in range(m):
        f = False
        for c in range(n):
            if grid[r][c] in turn:
                f = True
                break
        if f:
            break

    visited.add((r, c))
    t = grid[r][c]
    x, y = directions[t]

    while (0 <= r < m) and (0 <= c < n):
        visited.add((r, c))

        if (0 <= r + x < m) and (0 <= c + y < n) and grid[r + x][c + y] == "#":
            t = turn[t]
            x, y = directions[t]
        else:
            r, c = r + x, c + y

    return len(visited)


def main():
    print(run_trace(read_file("input.txt")))


main()
