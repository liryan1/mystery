#include <vector>
#include <queue>
using namespace std;

class Solution
{
private:
    struct Point
    {
        int x, y;
    };
    vector<Point> neighbors(Point &p, int m, int n)
    {
        vector<Point> N;
        int row[] = {-1, 0, 0, 1}, col[] = {0, -1, 1, 0};
        for (int r = 0; r < 4; r++)
        {
            int x = p.x + row[r], y = p.y + col[r];
            if (x >= 0 && x < m && y >= 0 && y < n)
            {
                N.push_back(Point{x, y});
            }
        }
        return N;
    }
    void BFS(vector<vector<char>> &g, vector<vector<bool>> &v, Point p)
    {
        int m = g.size(), n = g[0].size();
        // DFS and marked visited
        queue<Point> q;
        q.push(p);
        while (!q.empty())
        {
            Point p = q.front();
            q.pop();
            if (v[p.x][p.y])
            {
                continue;
            }
            v[p.x][p.y] = true;
            for (auto &n : neighbors(p, m, n))
            {
                if (g[n.x][n.y] == '1')
                {
                    q.push(n);
                }
            }
        }
    }

public:
    int numIslands(vector<vector<char>> &grid)
    {
        int m = grid.size(), n = grid[0].size(), islands = 0;
        vector<vector<bool>> visited(m, vector<bool>(n, false));

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited[i][j] && grid[i][j] == '1')
                {
                    islands++;
                    BFS(grid, visited, Point{i, j});
                }
            }
        }
        return islands;
    }
};