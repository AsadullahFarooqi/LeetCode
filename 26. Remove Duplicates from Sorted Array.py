class Solution:
    def removeDuplicates(self, nums):
        # empty list
        if len(nums) <= 1:
            return len(nums)
        else:
            e_u_l = 1
            for i in range(1, len(nums)):
                if nums[e_u_l-1] != nums[i]:
                    nums[e_u_l] = nums[i]
                    e_u_l += 1
                    
        return e_u_l

        
    def other_best_way(self, nums):
        if not nums:
            return 0
        end_of_uniq_list = 1
        for iterator in range(1, len(nums)):
            if nums[end_of_uniq_list-1] != nums[iterator]:
                nums[end_of_uniq_list] = nums[iterator]
                end_of_uniq_list += 1
        return end_of_uniq_list


if __name__ == '__main__':
    n = [0,0,1,1,1,2,2,3,3,4]
    n = [1,1,2]
    sol = Solution().other_best_way(n)
    print(n[:sol])
    