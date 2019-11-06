class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if not i in d:
                d[i] = 0
            d[i] += 1
            
        for v in d.values():
            if v > 1:
                return True
                
        return False