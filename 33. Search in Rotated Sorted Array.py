def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # go left
    if not len(nums): return -1
    if nums[0] > target:
        i = 0
        while abs(i) < len(nums) and nums[i] >= target:
            if nums[i] == target:
                return len(nums) + i
            i -= 1
        return -1
    else:
    	print("im here")
        i = 0
        while abs(i) < len(nums) and nums[i] <= target:
            if nums[i] == target:
                return i
            i += 1
        return -1


if __name__ == '__main__':
    n,t = [4,5,6,7,0,1,2],6
    # n,t = [1], 2
    print(search(n, t))