class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # DFS + 访问数组 + 方向数组
        if not grid:
            return 0
        # m = rows, n = columns
        m, n = len(grid), len(grid[0])
        visited = set()
        numberOfIsland = 0
        dirs = [
            (0, 1),    # right
            (0, -1),   # left
            (1, 0),    # down
            (-1, 0),   # up
        ]

        for i in range(m):
            for j in range(n):
                # 这里对该点进行有效性检查: eg：是否越界，是否是1，是否被访问过
                if self.check(grid, i, j, visited):
                    # dfs search the island, and mark them as visited
                    self.dfs(grid, i, j, visited, dirs)
                    numberOfIsland += 1
        return numberOfIsland

    def dfs(self, grid, x, y, visited, dirs):
        visited.add((x, y))  # 把该点加入到visited里
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if self.check(grid, nx, ny, visited):
                self.dfs(grid, nx, ny, visited, dirs)

    def check(self, grid, x, y, visited):
        m, n = len(grid), len(grid[0])
        # python中， 1 是True， 0 是False
        if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] and (x, y) not in visited:
            return True

        return False
