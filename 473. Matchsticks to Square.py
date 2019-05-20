def makesquare(nums: List[int]) -> bool:
    if len(nums) < 4: return False

    s1, s2, s3, s4 = 0,0,0,0
    nums = sorted(nums, reverse=True)
    max_ = nums[0]
    i = 0
    while i <= len(nums):
      s1 += i
