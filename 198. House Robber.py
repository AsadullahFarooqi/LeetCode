class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(sum(nums[::2]), sum(nums[1:][::2]))


if __name__ == '__main__':
    l = [1,2,3,1]
    l = [2,7,9,3,1]
    sol = Solution().rob(l)
    print(sol)