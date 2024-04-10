class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(r, c, index):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                return 0
            grid[r][c] = index
            return 1 + sum(dfs(r + dr, c + dc, index) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)])

        index = 2
        island_sizes = {0: 0}
        max_island_size = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    size = dfs(i, j, index)
                    island_sizes[index] = size
                    max_island_size = max(max_island_size, size)
                    index += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    neighbors = set(grid[nr][nc] for nr, nc in
                                    [(i + dr, j + dc) for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)] if
                                     0 <= i + dr < len(grid) and 0 <= j + dc < len(grid[0])])
                    max_island_size = max(max_island_size, sum(island_sizes[n] for n in neighbors) + 1)

        return max_island_size
