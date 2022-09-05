from typing import List

class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        unique_paths = [[0 for j in range(n)] for i in range(m)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j] == 1:
                    unique_paths[i][j] = 0
                else:
                    if i == m - 1 and j == n - 1:
                        unique_paths[i][j] = 1

                    else:
                        unique_paths_right = (
                            unique_paths[i][j + 1]
                            if j < n - 1
                            else 0
                        )

                        unique_paths_below = (
                            unique_paths[i + 1][j]
                            if i < m - 1
                            else 0
                        )

                        unique_paths[i][j] = unique_paths_right + unique_paths_below

        return unique_paths[0][0]

class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        unique_paths = [0] * n

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j] == 1:
                    unique_paths[j] = 0
                else:
                    if i == m - 1 and j == n - 1:
                        unique_paths[j] = 1

                    else:
                        unique_paths_right = (
                            unique_paths[j + 1]
                            if j < n - 1
                            else 0
                        )

                        unique_paths_below = (
                            unique_paths[j]
                            if i < m - 1
                            else 0
                        )

                        unique_paths[j] = unique_paths_right + unique_paths_below

        return unique_paths[0]

def main() -> None:
    test_cases = [
        [[0,0,0],[0,1,0],[0,0,0]],
        [[0,1],[0,0]],
    ]

    solution = Solution2();

    for inputs in test_cases:
        obstacleGrid = inputs

        test = solution.uniquePathsWithObstacles(obstacleGrid)

        print(test)

if __name__ == '__main__':
    main()
