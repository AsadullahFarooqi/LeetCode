class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid or not len(grid[0]):
            return 0
        
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans += self.is_island(grid, row, col)
        return ans
    
        
    def is_island(self, grid, r, c):
        if c < 0 or c >= len(grid[0]) or r < 0 or r >= len(grid) or grid[r][c] == "0":
            return 0
        grid[r][c] = "0"
        # go left
        self.is_island(grid, r, c-1)
        # go right
        self.is_island(grid, r, c+1)
        # go up
        self.is_island(grid, r-1, c)
        # go down
        self.is_island(grid, r+1, c)
        
        return 1

if __name__ == '__main__':
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution().numIslands(grid)
    print(sol)

"""
This question was in book.

- I saw this question in a book. for preparing for the technical interview.
- It was in a book but can be asked in interview.
- Medium or may be Easy.
- It requires clever recursive thinking.



Pascal's Triangle II

[[1], [2,3], [4,1,1]]


Given a pyramid of positive inteagers and a Target. Find a path in the pyramid that traverses the pyramid from top to bottom visiting numbers whose product is a given target value. Each step in the path must go down one row, and go either one step to the left or one step to the right.

Example 1:

`pyramid = [[1], [2,3], [4,1,1]]` , `target = 2`
        1       
    2       3   
4       1       1

return `[1,2,1]`

Example 2:

`pyramid = [[1], [1,1], [6,3,2], [4,3,3,7]], target = 6`
             1       
         1       1   

    6       3       2      

4       3       3      7

return `[1,3,2,1]`

"""