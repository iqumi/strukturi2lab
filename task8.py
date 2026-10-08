SIZE = 4
BOX = 2
EMPTY = 0


def find_empty(matrix: list[list[int]]) -> tuple[int, int] | None:
    for row in range(SIZE):
        for col in range(SIZE):
            if matrix[row][col] == EMPTY:
                return row, col
    return None


def is_valid(matrix: list[list[int]], row: int, col: int, value: int) -> bool:
    if value in matrix[row]:
        return False
    if any(matrix[r][col] == value for r in range(SIZE)):
        return False
    box_row = row - row % BOX
    box_col = col - col % BOX
    return all(
        matrix[r][c] != value
        for r in range(box_row, box_row + BOX)
        for c in range(box_col, box_col + BOX)
    )


def solve_sudoku(matrix: list[list[int]]) -> bool:
    position = find_empty(matrix)
    if position is None:
        return True

    row, col = position
    for value in range(1, SIZE + 1):
        if is_valid(matrix, row, col, value):
            matrix[row][col] = value
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = EMPTY
    return False


def main() -> None:
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4],
    ]
    if solve_sudoku(matrix):
        for row in matrix:
            print("".join(map(str, row)))
    else:
        print("Решения нет")


if __name__ == "__main__":
    main()
