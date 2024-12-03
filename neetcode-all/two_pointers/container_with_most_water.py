class Solution:
    def maxArea(self, height: List[int]) -> int:
        #O(n) time, O(1) space 
        res = 0 
        l, r = 0, len(height) - 1

        for i in range(len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(area, res)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
