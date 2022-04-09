from tkinter import Y
from typing import List

class Solution:
    def pacific(self, m: int, n: int) -> List[List[int]]:
        '''Points of Left and Top boundaries'''
        points = []
        for i in range(m):
            points.append([i, 0])
        for j in range(n):
            points.append([0, j])
        return points

    def atlantic(self, m: int, n: int) -> List[List[int]]:
        '''Points of Right and Lower boundaries'''
        points = []
        for i in range(m):
            points.append([i, n-1])
        for j in range(n):
            points.append([m-1, j])
        return points

    def valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n

    def get_nb(self, x, y, m, n):
        row, col = [-1, 0, 0, 1], [0, -1, 1, 0]
        return [[x+r, y+c] for r, c in zip(row, col) if self.valid(x+r, y+c, m, n)]

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(initial_points, ocean) -> None:
            '''DFS through heights and modify flow array'''
            s = initial_points
            while s:
                x, y = s.pop()
                if flow[x][y] == ocean:
                    continue

                # for second DFS, add the point that can reach both oceans
                if ocean == "A" and flow[x][y] == "P":
                    both.append([x, y])
                flow[x][y] = ocean
                for i, j in self.get_nb(x, y, m, n):
                    if heights[i][j] >= heights[x][y]:
                        s.append([i, j])

        both = []
        m, n = len(heights), len(heights[0])
        flow = [[""]*n for _ in range(m)]

        dfs(self.pacific(m, n), "P")
        dfs(self.atlantic(m, n), "A")

        return both
