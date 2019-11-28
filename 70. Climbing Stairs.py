class Solution(object):
    def climbStairs(self, n):
        if n == 1: return 1
        elif n == 2: return 2

        n_minus_2 = 1
        n_minus_1 = 2
        for i in range(2, n-1):
            new = n_minus_2 + n_minus_1
            n_minus_2 = n_minus_1
            n_minus_1 = new
        return n_minus_2 + n_minus_1

if __name__ == '__main__':
    inp = 5
    sol = Solution().climbStairs(inp)
    print(sol)