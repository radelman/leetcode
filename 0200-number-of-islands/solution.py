from typing import List

class Solution:
    def fill(self, grid: List[List[str]], i: int, j: int, value: int) -> None:
        grid[i][j] = value

        if i > 0 and grid[i - 1][j] == "1":
            self.fill(grid, i - 1, j, value)

        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.fill(grid, i + 1, j, value)

        if j > 0 and grid[i][j - 1] == "1":
            self.fill(grid, i, j - 1, value)

        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            self.fill(grid, i, j + 1, value)

    def numIslands(self, grid: List[List[str]]) -> int:
        next_island_id = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.fill(grid, i, j, next_island_id)
                    next_island_id += 1

        return next_island_id - 1

def main() -> None:
    test_cases = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"],
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"],
        ]
    ]

    solution = Solution();

    for inputs in test_cases:
        grid = inputs

        test = solution.numIslands(grid)

        print(test)

if __name__ == '__main__':
    main()
