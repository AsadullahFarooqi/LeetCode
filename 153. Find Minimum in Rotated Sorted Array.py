def search(nums):
    # go left
        if not len(nums): return -1
        elif len(nums) <= 8:
            return min(nums)
        # compare the first middle end element
        i = 0
        for j in [0, len(nums)//2, len(nums)-1]:
            if nums[j] < nums[i]:
                i = j

        prev = nums[i-1]
        if prev > nums[i]:
            i = 0
            while abs(i) < len(nums) and nums[i] < target:
                target = nums[i]
                i -= 1
            return target
        else:
            i = 0
            while abs(i) < len(nums) and target > nums[i]:
                i += 1
                target = nums[i-1]
            return target


if __name__ == '__main__':
    # n= [4,5,6,7,0,1,2]
    n = [1,2,3,4,5,6]
    print(search(n))