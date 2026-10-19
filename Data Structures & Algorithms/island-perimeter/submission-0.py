from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) # rows, columns

        # i think we can use bfs to count the number of squares
        # and each neighbour of a sqaure removes one side that wouldve added to the perimeter

        queue = deque([])
        visited = set()
        perimeter = 0

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))

        while queue:
            i, j = queue.pop()
            count = 4
            for di, dj in directions:
                ni, nj = i+di, j+dj

                if (0<=ni<m and 0<=nj<n and grid[ni][nj]==1):
                    count -=1
            perimeter += count

        return perimeter