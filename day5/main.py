from collections import defaultdict


def read_file(file_name: str) -> tuple[dict[list[str]], list[list[str]]]:
    graph, updates = defaultdict(list), []

    with open(file_name) as f:
        # first section
        for line in f:
            if line.strip() == "":
                break
            bf, af = line.strip().split("|")
            graph[af].append(bf)

        # second section
        for line in f:
            if line.strip() != "":
                updates.append(line.strip().split(","))

    return graph, updates


def check_updates(graph: dict[list[str]], updates: list[list[str]]) -> int:
    def check_update(update: list[str]) -> bool:
        update_set, acc_set = set(update), set()
        for u in update:
            for prereq in graph[u]:
                if prereq in update_set and prereq not in acc_set:
                    return False
            acc_set.add(u)
        return True

    ans = 0
    for update in updates:
        if check_update(update):
            if not len(update) % 2:
                print("huhh its even")
            else:
                ans += int(update[len(update) // 2])
    return ans


def main():
    print(check_updates(*read_file("input.txt")))


main()
