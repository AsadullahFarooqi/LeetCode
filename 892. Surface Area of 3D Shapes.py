"""892. Surface Area of 3D Shapes

    On a N * N grid, we place some 1 * 1 * 1 cubes.
    Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).
    Return the total surface area of the resulting shapes.

    Example 1:
    Input: [[2]]
    Output: 10

    Example 2:
    Input: [[1,2],[3,4]]
    Output: 34

    Example 3:
    Input: [[1,0],[0,2]]
    Output: 16

    Example 4:
    Input: [[1,1,1],[1,0,1],[1,1,1]]
    Output: 32

    Example 5:
    Input: [[2,2,2],[2,1,2],[2,2,2]]
    Output: 46
    
    Note:
    1 <= N <= 50
    0 <= grid[i][j] <= 50
"""

class Solution:

    def surfaceArea(self, grid):
        tower_area = lambda t: 2 + 4*t
        n = len(grid)
        ans = 0
        for row in range(n):
            for col in range(n):
                ans = tower_area(grid[row][col])
                

        for row in range(n):
            for col in range(n):
                ans -= grid[row][col]

        print(ans)

if __name__ == '__main__':
    l = [[1,2],[3,4]]
    solution = Solution()
    print(solution.surfaceArea(l))