def findUnsortedSubarray(nums):
        # finding start
        s = 0
        while s < len(nums)-1 and nums[s] <= nums[s+1]:
            s += 1

        # finding end
        e = len(nums)-1
        while e > 0 and nums[e] >= nums[e-1]:
            e -= 1

        return len(nums[s:e+1])

if __name__ == '__main__':
    # n = [2, 6, 4, 8, 10, 9, 15]
    # n = [1,2,3,4]
    n = [1,2,3,3,3]
    print(findUnsortedSubarray(n))