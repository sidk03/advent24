def read_file(file_name: str) -> list[list[str]]:
    lines = []
    with open(file_name) as f:
        lines = f.readlines()
    return [list(line.strip()) for line in lines]


def count_xmas(grid: list[list[str]]) -> int:
    target = "XMAS"
    m, n = len(grid), len(grid[0])

    def search_xmas(r, c, dx, dy):
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


def main():
    print(count_xmas(read_file("input.txt")))


main()
