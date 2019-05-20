def findDisappearedNumbers(nums):
    for num in nums:
        num = abs(num)
        if nums[num-1] >0:
            nums[num-1] *=-1
    print(nums)
    return [i+1 for i,x in enumerate(nums) if x>0]

# using counting sort technique
def my_alg(nums):
    print(nums)
    c = [0 for i in range(len(nums))]
    for i in nums:
        c[i-1] += 1
    return [i+1 for i,x in enumerate(c) if x==0]

if __name__ == '__main__':
    list_ = [2,5,3,8,2,3,8,3]
    # for i, x in enumerate(list_):
    #   print(i, x)
    print(my_alg(list_))
    # print(findDisappearedNumbers(list_))