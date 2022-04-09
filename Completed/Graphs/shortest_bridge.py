from collections import deque
from typing import List

class Solution:
    def valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def get_nb(self, x, y, m, n):
        row, col = [-1, 0, 0, 1], [0, -1, 1, 0]
        return [[x+r, y+c] for r, c in zip(row, col) if self.valid(x+r, y+c, m, n)]
    
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def get_island1_coords(q1, m, n):
            island_coords = [(*q1[0],0)]
            while q1:
                x, y = q1.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = 1
                grid[x][y] = 2
                for i, j in self.get_nb(x, y, m, n):
                    if grid[i][j] == 1:
                        island_coords.append((i, j, 0))
                        q1.append((i, j))
            return island_coords
                
        m, n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    q1 = deque([(i, j)])
                    # all island1 coordinates are labelled 2
                    island_coords = get_island1_coords(q1, m, n)
                    break
            else: # if inner loop does not break, outer loop continues
                continue
            break
            
        if not island_coords: return -1
        q = deque(island_coords)
        visited = [[0]*n for _ in range(m)]
        
        while q:
            x, y, d = q.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = 1
            if grid[x][y] == 1:
                return d - 1
            for i, j in self.get_nb(x, y, m, n):
                if grid[i][j] != 2:
                    q.append((i, j, d + 1))
    
        return -1