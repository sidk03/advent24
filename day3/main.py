import re


def read_file(file_name: str) -> str:
    lines = []
    with open(file_name) as f:
        lines = f.readlines()
    return lines


def find_matches(lines: list[str]) -> list[tuple[str, str]]:
    ans = []
    for line in lines:
        ans.extend(re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line))
    return ans


def find_answer(pairs: list[tuple[int, int]]) -> int:
    return sum(int(x) * int(y) for x, y in pairs)


def main():
    print(find_answer(find_matches(read_file("input.txt"))))


main()
