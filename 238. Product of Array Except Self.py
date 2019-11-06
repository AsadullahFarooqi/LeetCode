class Solution:
    def productExceptSelf(self, nums):
        ans = [i for i in nums]
        for i in range(len(nums)-2, -1, -1):
            ans[i] = ans[i] * ans[i+1]

        prev = 1
        for curr in range(len(nums)-1):
            ans[curr] = prev * ans[curr+1]
            prev *= nums[curr]
            
        ans[curr+1] = prev
        return ans


if __name__ == '__main__':
    n = [2,3,4,5] #[1,2,3,4]
    sol = Solution().productExceptSelf(n)
    print(sol)