def checkposs(nums):
        t = 0
        for i in range(1, len(nums)):
            if t > 1: return False
            elif nums[i] <= nums[i-1]: t += 1
        return (t-1) == 0
if __name__ == '__main__':
    n = [-1,4,2,3] # [4,2,3]
    print(checkposs(n))