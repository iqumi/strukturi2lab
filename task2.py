def tribonacci(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


def main() -> None:
    print([tribonacci(n) for n in range(17)])


if __name__ == "__main__":
    main()
