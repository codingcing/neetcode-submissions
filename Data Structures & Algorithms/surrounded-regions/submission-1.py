from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])

        edge = deque()
        not_surrounded = set()
        for i in range(m):
            for j in range(n):
                if i in [0,m-1] or j in [0,n-1]:
                    if board[i][j] == 'O':
                        edge.append((i,j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while edge:
            x, y = edge.popleft()
            not_surrounded.add((x, y))
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0<=new_x<m and 0<=new_y<n and (new_x, new_y) not in not_surrounded:
                    if board[new_x][new_y] == 'O':
                        edge.append((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if (i,j) not in not_surrounded:
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
        
        return