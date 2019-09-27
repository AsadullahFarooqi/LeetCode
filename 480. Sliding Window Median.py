from bisect import insort
from heapq import *

class Solution:
    def maxSlidingWindow(self, nums, k):
        m = k//2
        window = sorted(nums[:k])
        medians = []
        for left, right in zip(nums, nums[k:]+[0]):
            # medians.append((window[m] + window[int(m - (k%2 == 0))]) / 2.0)
            medians.append((window[m] + window[~m]) / 2.)
            window.remove(left)
            insort(window, right)

        return medians


class StefanPochmanSolution:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class StefanPochmanSolutionShort:

    def __init__(self):
        self.heaps = None, [], []
        self.i = 1

    def addNum(self, num):
        heappush(self.heaps[-self.i], -heappushpop(self.heaps[self.i], num * self.i))
        self.i *= -1

    def findMedian(self):
        return (self.heaps[self.i][0] * self.i - self.heaps[-1][0]) / 2.0

if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    sol = Solution()

    print(sol.maxSlidingWindow(nums,k))
