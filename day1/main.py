def read_file(file_name: str) -> tuple[list[str], list[str]]:
    l1, l2 = [], []
    with open(file_name) as f:
        for x in f:
            v1, v2 = x.split()
            l1.append(v1), l2.append(v2)
    return l1, l2


def sort_sum_lists(l1: list[str], l2: list[str]) -> int:
    return sum(abs(int(x) - int(y)) for x, y in zip(sorted(l1), sorted(l2)))


def main() -> None:
    return sort_sum_lists(*read_file("input.txt"))


print(main())
