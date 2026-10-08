import random
import sys
import time
from statistics import median
from typing import Callable

import matplotlib.pyplot as plt

SIZES = list(range(100, 2001, 100))
REPEATS = 3
SEED = 42

sys.setrecursionlimit(10_000)


def selection_sort(array: list[int]) -> list[int]:
    result = array.copy()
    for i in range(len(result) - 1):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result


def quicksort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def random_data(size: int) -> list[int]:
    return [random.randint(0, size * 10) for _ in range(size)]


def sorted_data(size: int) -> list[int]:
    return sorted(random_data(size))


def reversed_data(size: int) -> list[int]:
    return sorted(random_data(size), reverse=True)


def measure(sort: Callable[[list[int]], list[int]], data: list[int]) -> float:
    timings = []
    for _ in range(REPEATS):
        start = time.perf_counter()
        sort(data)
        timings.append(time.perf_counter() - start)
    return median(timings)


def build_plot(
    title: str,
    file_name: str,
    generator: Callable[[int], list[int]],
) -> None:
    selection_times = []
    quick_times = []
    for size in SIZES:
        data = generator(size)
        selection_times.append(measure(selection_sort, data))
        quick_times.append(measure(quicksort, data))

    plt.figure(figsize=(8, 5))
    plt.plot(SIZES, selection_times, marker="o", label="Сортировка выбором")
    plt.plot(SIZES, quick_times, marker="s", label="Быстрая сортировка")
    plt.title(title)
    plt.xlabel("Размер входных данных")
    plt.ylabel("Время выполнения, с")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(file_name, dpi=150)
    plt.close()


def main() -> None:
    random.seed(SEED)
    build_plot("Случайный список", "task1_random.png", random_data)
    build_plot("Отсортированный список", "task1_sorted.png", sorted_data)
    build_plot(
        "Список, отсортированный в обратном порядке",
        "task1_reversed.png",
        reversed_data,
    )


if __name__ == "__main__":
    main()
