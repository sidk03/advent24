from collections import Counter
from functools import reduce


def read_file(file_name: str) -> tuple[list[int], list[int]]:
    l1, l2 = [], []
    with open(file_name) as f:
        for x in f:
            v1, v2 = x.split()
            l1.append(v1), l2.append(v2)
    return map(int, l1), map(int, l2)


def sort_sum_lists(l1: list[int], l2: list[int]) -> int:
    return sum(abs(x - y) for x, y in zip(sorted(l1), sorted(l2)))


def similarity_check(l1: list[int], l2: list[int]) -> int:
    count = Counter(l2)
    return reduce(lambda acc, num: acc + (num * count.get(num, 0)), l1, 0)


def main() -> None:
    print(sort_sum_lists(*read_file("input.txt")))
    print(similarity_check(*read_file("input.txt")))


main()
