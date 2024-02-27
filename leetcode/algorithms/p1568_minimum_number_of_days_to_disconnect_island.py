from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        if self._number_of_islands(grid) != 1:
            return 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0

                    if self._number_of_islands(grid) != 1:
                        return 1

                    grid[i][j] = 1

        return 2

    def _number_of_islands(self, grid: List[List[int]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

                    self._dfs(grid, i, j, visited)

        return count

    def _dfs(self, grid, row, column, visited):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return

        visited[row][column] = True

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(grid, row + direction[0], column + direction[1], visited)
