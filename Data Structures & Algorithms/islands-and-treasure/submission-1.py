from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        INF = 2**31 - 1
        if not m or not n: return
        q = deque()
        # add all treasure chests and then multiple BFS out from them
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0<=new_x<m and 0<=new_y<n and grid[new_x][new_y] == INF:
                    grid[new_x][new_y] = 1 + grid[x][y]
                    q.append((new_x, new_y))
        
        return