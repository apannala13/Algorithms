class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #O(n log n) time 
        if len(nums) == 1:
            return 0

        nums.sort()
        l = 0 
        min_diff = float('inf')

        #k - 1 to start at the end for max elements 
        for r in range(k - 1, len(nums)):
            min_diff = min(min_diff, nums[r] - nums[l])
            l += 1
        return min_diff
