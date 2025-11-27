from functools import reduce
from typing import Callable


def read_file(file_name: str) -> list[list[int]]:
    l = []
    with open(file_name) as f:
        for x in f:
            l.append(x.strip().split(" "))
    return list(map(lambda x: list(map(int, x)), l))


def violation_idx(l: list[int]):
    inc, dec = False, False
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            inc = True
        else:
            dec = True
        if (inc and dec) or not (1 <= abs(l[i] - l[i - 1]) <= 3):
            return i

    return -1


def is_safe_report(l: list[int]):
    return 1 if violation_idx(l) == -1 else 0


def is_safe_report_damp(l: list[int]):
    idx = violation_idx(l)
    if idx == -1:
        return 1
    return (
        1
        if reduce(
            lambda acc, l: acc or l == -1,
            map(violation_idx, [l[:idx] + l[idx + 1 :], l[: idx - 1] + l[idx:], l[1:]]),
            False,
        )
        else 0
    )


def count_safe_reports(l: list[list[int]], f: Callable[[list[int]], int]) -> int:
    return reduce(lambda acc, report: acc + f(report), l, 0)


def main() -> None:
    print(count_safe_reports(read_file("input.txt"), is_safe_report))
    print(count_safe_reports(read_file("input.txt"), is_safe_report_damp))


main()
