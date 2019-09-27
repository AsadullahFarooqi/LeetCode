from bisect import insort

class Solution:
    def maxSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        ans = []

        for left, right in zip(nums, nums[k:] + [0]):
            ans.append(window[-1])
            window.remove(left)
            insort(window, right)

        return ans


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()

    print(sol.maxSlidingWindow(nums,k))