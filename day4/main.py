def read_file(file_name: str) -> list[list[str]]:
    lines = []
    with open(file_name) as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]


def count_xmas(grid: list[list[str]]) -> int:
    target = "XMAS"
    m, n = len(grid), len(grid[0])

    def search_xmas(r: int, c: int, dx: int, dy: int) -> bool:
        for i in range(4):
            x, y = r + (i * dx), c + (i * dy)
            if not (0 <= x < m) or not (0 <= y < n) or grid[x][y] != target[i]:
                return False
        return True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for r in range(m):
        for c in range(n):
            for dx, dy in directions:
                if search_xmas(r, c, dx, dy):
                    count += 1
    return count


def count_xmas_X(grid: list[list[str]]) -> int:
    target_1 = "MAS"
    target_2 = "SAM"
    m, n = len(grid), len(grid[0])

    def check_diagonal(r: int, c: int, target: str, dir: list[int]) -> bool:
        x, y = dir
        for i in range(3):
            if target[i] != grid[r + (i * x)][c + (i * y)]:
                return False
        return True

    def search_xmas(r: int, c: int):
        if r + 2 < m and c + 2 < n:
            if (
                check_diagonal(r, c, target_1, [1, 1])
                or check_diagonal(r, c, target_2, [1, 1])
            ) and (
                check_diagonal(r, c + 2, target_1, [1, -1])
                or check_diagonal(r, c + 2, target_2, [1, -1])
            ):
                return True
        return False

    count = 0
    for r in range(m):
        for c in range(n):
            if search_xmas(r, c):
                count += 1
    return count


def count_xmas_X_opt(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    count = 0
    for r in range(1, m - 1):
        for c in range(1, n - 1):
            if grid[r][c] == "A":
                tl, tr = grid[r - 1][c - 1], grid[r - 1][c + 1]
                bl, br = grid[r + 1][c - 1], grid[r + 1][c + 1]
                if {tl, br} == {"M", "S"} and {tr, bl} == {"M", "S"}:
                    count += 1
    return count


def main():
    print(count_xmas(read_file("input.txt")))
    print(count_xmas_X(read_file("input.txt")))
    print(count_xmas_X_opt(read_file("input.txt")))


main()
