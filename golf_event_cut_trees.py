''' Solution for Leetcode gold event problem. Unfortunately, Time limit exceeded...
'''

from collections import deque


def cutOffTree(forest: list[list[int]]) -> int:
    # Get and sort trees
    trees = []
    for r, row in enumerate(forest):
        for c, v in enumerate(row):
            if v > 1:
                trees.append((v, r, c))
    trees.sort()

    curr_x = curr_y = ans = 0
    for _, x, y in trees:
        d = BFS(forest, curr_x, curr_y, x, y)
        if d < 0:
            return -1
        ans += d
        curr_x, curr_y = x, y
    return ans

def BFS(self, forest, x0, y0, x1, y1):
    ''' BFS through array
    Return the number of steps required to reach x, y from
    x0, y0
    '''
    m, n = len(forest), len(forest[0])
    visited = {}
    q = deque([(x0, y0, 0)])
    while q:
        x, y, d = q.pop()
        visited.add((x, y))
        if x == x1 and y == y1:
            return d
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= i < m and 0 <= j < n and \
                (i, j) not in visited and forest[i][j] != 0:
                q.appendleft((i, j, d+1))
    return -1
