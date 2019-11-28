class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not len(grid[0]):
            return 0
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    area = self.is_island(grid, row, col)
                    max_area = max(max_area, area)
        return max_area
    
        
    def is_island(self, grid, r, c):
        if c < 0 or c >= len(grid[0]) or r < 0 or r >= len(grid) or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        # go left
        left = self.is_island(grid, r, c-1)
        # go right
        right = self.is_island(grid, r, c+1)
        # go up
        up = self.is_island(grid, r-1, c)
        # go down
        down = self.is_island(grid, r+1, c)
        
        return 1+left + right + up + down
        # return 1+self.is_island(grid, r, c-1) + self.is_island(grid, r, c+1) + self.is_island(grid, r-1, c) + self.is_island(grid, r+1, c)

if __name__ == '__main__':
    g = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    g = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    g = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution().maxAreaOfIsland(g)
    print(sol)