def findErrorNums(nums):
        duplicat, miss = None, None
        nums = sorted(nums)
        for p in range(1, len(nums)):
            if nums[p-1] == nums[p]:
                duplicat = nums[p]
        i = 1
        for v in range(len(nums)):
            print(i,nums[v])
            if i != nums[v] and nums[v] == duplicat:
                continue
            if i != nums[v]:
                miss = i
                break
            i += 1
        if not miss: miss = i
        return [duplicat, miss]

if __name__ == '__main__':
    nums = [1,2,2,4]
    # nums = [2,2]
    # nums = [1,2,3,4,6,6,5]
    # nums = [3,2,3,4,6,5]
    # nums = [1,5,3,2,2,7,6,4,8,9]
    print(findErrorNums(nums))
"""
    nums = sorted(nums)
    for i in range(1, len(nums)+1):
        if nums[i-1] != i:
            return [nums[i-1], i]
"""