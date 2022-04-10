'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''

class Solution:
    def valid(self, x: int, y: int, m: int, n: int) -> bool:
        return 0 <= x < m and 0 <= y < n

    def get_nb(self, x: int, y: int, m: int, n: int) -> list[list[int]]:
        row, col = [-1, 0, 0, 1], [0, -1, 1, 0]
        return [[x+r, y+c] for r, c in zip(row, col) if self.valid(x+r, y+c, m, n)]

    def on_edge(self, x: int, y: int, m: int, n: int) -> bool:
        return x == 0 or x == m - 1 or y == 0 or y == n - 1

    def dfs(self, board: list[list[int]], visited: list[list[int]], i: int, j: int) -> list[list[int]]:
        m, n = len(board), len(board[0])
        stack = [(i, j)]
        path = []
        touching_edge = False
        while stack:
            r, c = stack.pop()
            if visited[r][c]:
                continue
            visited[r][c] = 1
            path.append([r, c])
            if self.on_edge(r, c, m, n):
                touching_edge = True

            for i, j in self.get_nb(r, c, m, n):
                if board[i][j] == "O":
                    stack.append((i, j))
        return path if not touching_edge else []

    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[0]*n for _ in range(m)]
        surrounded = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    surrounded += self.dfs(board, visited, i, j)

        for i, j in surrounded:
            board[i][j] = "X"

        return
