def firstMissingPositive(nums):
        # if len(nums) == 0: 
        #     return 1
        # elif len(nums) == 1 and nums[0] > 1:
        #     return 1

        missing_min = None
        arr = set()
        for i in nums:
            if i > 0:
                arr.add(i)
        j = 1
        arr = sorted(list(arr))
        print(arr)
        for p in arr:
            if j != p:
                print('im here')
                return j
            j += 1
        return j

if __name__ == '__main__':
    # n = [2147483647]
    # n = [3,4,-1,1]
    # n = [7,8,9,11,12]
    # n = [1,2,0]
    n = [1, 10000]
    print(firstMissingPositive(n))