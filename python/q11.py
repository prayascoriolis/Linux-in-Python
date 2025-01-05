"""11. Write a function to solve a Sudoku puzzle (validate the grid format only)."""


def is_valid_sudoku(grid):
    """
    Args:
        grid: A 9x9 grid representing a Sudoku puzzle.
    Returns:
        bool: True / False
    """
    # Validate the grid size
    if not (
        isinstance(grid, list) and len(grid) == 9 and all(len(row) == 9 for row in grid)
    ):
        return False

    # Helper function to check for duplicates
    def has_duplicates(nums):
        nums = [n for n in nums if n != 0 and n is not None]
        return len(nums) != len(set(nums))

    # Validate rows and columns
    for i in range(9):
        if has_duplicates(grid[i]):
            return False
        if has_duplicates([grid[j][i] for j in range(9)]):
            return False

    # Validate subgrids (3x3 blocks)
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            subgrid = [
                grid[r][c]
                for r in range(box_row, box_row + 3)
                for c in range(box_col, box_col + 3)
            ]
            if has_duplicates(subgrid):
                return False

    return True


if __name__ == "__main__":
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print(is_valid_sudoku(sudoku_grid))
