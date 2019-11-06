class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            e_u_l = 1
            for i in range(1, len(nums)):
                if nums[e_u_l-1] != nums[i]:
                    nums[e_u_l] = nums[i]
                    e_u_l += 1
                    
        return e_u_l