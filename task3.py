def recursive_count(some_list: list, t) -> int:
    def rcount(lo: int, hi: int) -> int:
        if lo == hi:
            return 1 if some_list[lo] == t else 0

        mid = (lo + hi) // 2
        left = rcount(lo, mid)
        right = rcount(mid + 1, hi)
        return left + right

    if not some_list:
        return 0
    return rcount(0, len(some_list) - 1)


def main() -> None:
    print(recursive_count([1, 2, 3, 2, 2, 5, 2], 2))
    print(recursive_count([1, 2, 3], 7))
    print(recursive_count([], 1))
    print(recursive_count(["a", "b", "a"], "a"))


if __name__ == "__main__":
    main()
