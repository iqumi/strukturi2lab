import time

import matplotlib.pyplot as plt

MAX_N = 40


def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int) -> int:
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def fib_with_lucas(n: int) -> int:
    if n <= 3:
        return fibonacci(n)
    i = n // 2
    j = n - i
    return (fib_with_lucas(i) * lucas_with_fib(j)
            + fib_with_lucas(j) * lucas_with_fib(i)) // 2


def lucas_with_fib(n: int) -> int:
    if n == 0:
        return 2
    return fib_with_lucas(n - 1) + fib_with_lucas(n + 1)


def measure(function, n: int) -> float:
    start = time.perf_counter()
    function(n)
    return time.perf_counter() - start


def check_correctness() -> None:
    for n in range(26):
        assert fibonacci(n) == fib_with_lucas(n)
        assert lucas(n) == lucas_with_fib(n)


def main() -> None:
    check_correctness()
    numbers = list(range(MAX_N + 1))
    fibonacci_times = [measure(fibonacci, n) for n in numbers]
    lucas_times = [measure(lucas, n) for n in numbers]
    fib_with_lucas_times = [measure(fib_with_lucas, n) for n in numbers]

    print(f"{'N':>3} {'fibonacci':>12} {'lucas':>12} {'fib_with_lucas':>16}")
    for n in numbers:
        print(f"{n:>3} {fibonacci_times[n]:>12.6f} {lucas_times[n]:>12.6f} "
              f"{fib_with_lucas_times[n]:>16.6f}")

    plt.figure(figsize=(8, 5))
    plt.plot(numbers, fibonacci_times, marker="o", label="fibonacci")
    plt.plot(numbers, lucas_times, marker="^", label="lucas")
    plt.plot(numbers, fib_with_lucas_times, marker="s", label="fib_with_lucas")
    plt.title("Время вычисления чисел Фибоначчи и Люка")
    plt.xlabel("N")
    plt.ylabel("Время выполнения, с")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("task4.png", dpi=150)
    plt.close()


if __name__ == "__main__":
    main()
