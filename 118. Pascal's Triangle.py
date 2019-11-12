"""
[
[1],
[1,1],
 [1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        ans = [[1]]
        row = 1
        prev_r_cols = 0
        while row <= numRows:
            r = [1]
            for c in range(1, prev_r_cols):
                r.append(ans[row-1][c-1] + ans[row-1][c])
            r.append(1)
            prev_r_cols += 1
            row += 1
        print(ans)

if __name__ == '__main__':
    k = 5
    sol = Solution().generate(k)