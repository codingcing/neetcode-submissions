from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = deque()
        visited_pacific = set()
        atlantic = deque()
        visited_atlantic = set()

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pacific.append((i,j))
                    visited_pacific.add((i,j))
                if i==m-1 or j==n-1:
                    atlantic.append((i,j))
                    visited_atlantic.add((i,j))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pacific:
            x,y = pacific.popleft()
            for dx, dy in directions:
                new_x = x+dx
                new_y = y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited_pacific and heights[new_x][new_y] >= heights[x][y]:
                    pacific.append((new_x,new_y))
                    visited_pacific.add((new_x,new_y))

        while atlantic:
            x,y = atlantic.popleft()
            for dx, dy in directions:
                new_x = x+dx
                new_y = y+dy
                if 0<=new_x<m and 0<=new_y<n and (new_x,new_y) not in visited_atlantic and heights[new_x][new_y] >= heights[x][y]:
                    atlantic.append((new_x,new_y))
                    visited_atlantic.add((new_x,new_y))

        return [[x,y] for (x,y) in visited_pacific if (x,y) in visited_atlantic]