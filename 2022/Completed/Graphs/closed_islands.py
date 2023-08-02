from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def on_edge(x, y):
            return x == 0 or x == m - 1 or y == 0 or y == n - 1
        
        def bfs(i, j):
            closed = 1
            q = deque([(i, j)])
            row, col = [-1, 0, 0, 1], [0, -1, 1, 0]
            while q:
                x, y = q.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = 1
                if on_edge(x, y):
                    closed = 0
                for r, c in zip(row, col):
                    i, j = x+r, y+c
                    if valid(i, j) and grid[i][j] == 0:
                        q.append((i, j))
            return closed
        
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        
        islands = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 0:
                    closed = bfs(i, j)
                    islands += closed
                    
        return islands