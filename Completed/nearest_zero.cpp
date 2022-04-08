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

public:
    // Update Matrix mat by putting in the distance to closest 0
    vector<vector<int>> updateMatrix(vector<vector<int>> &mat)
    {
        int m = mat.size(), n = mat[0].size(), i=0, j=0;
        queue<Point> q;
        vector<vector<int>> distance(m, vector<int>(n, -1));
        // Put all zero coordinates in q
        for (i = 0; i < m; ++i) {
            for (i = 0; j < n; ++j) {
                if (mat[i][j] == 0) {
                    q.push(Point{i, j});
                    distance[i][j] = 0;
                }
            }
        }
        while (!q.empty())
        {
            Point p = q.front();
            q.pop();
            for (auto &n : neighbors(p, m, n))
            {
                if (distance[n.x][n.y] == -1)
                {
                    distance[n.x][n.y] = distance[p.x][p.y] + 1;
                    q.push(n);
                }
            }
        }
        return distance;
    }

};