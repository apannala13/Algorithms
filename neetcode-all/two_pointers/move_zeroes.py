class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        #O(n) time 
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return nums 

        #brute force 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == 0 and nums[j] != 0:
        #             nums[i], nums[j] = nums[j], nums[i]
            
        # return nums 
