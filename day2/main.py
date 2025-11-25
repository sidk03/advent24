def read_file(file_name: str) -> list[list[str]]:
    l = []
    with open(file_name) as f:
        for x in f:
            l.append(x.split(" "))
    return l


def is_safe_report(l: list[str]) -> bool:
    inc, dec = False, False
    for i in range(1, len(l)):
        if int(l[i]) > int(l[i - 1]):
            inc = True
        else:
            dec = True
        if (inc and dec) or not (1 <= abs(int(l[i]) - int(l[i - 1])) <= 3):
            return False

    return True


def count_safe_reports(l: list[list[str]]) -> int:
    return sum(is_safe_report(ls) for ls in l)


def main() -> None:
    print(count_safe_reports(read_file("input.txt")))


main()
