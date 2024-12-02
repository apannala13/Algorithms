class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
      #O(n log(n)) - merge sort
        if len(nums) == 1:
            return nums
        
        middle = len(nums) // 2
        left, right = nums[:middle], nums[middle:]  

        left_subarray = self.sortArray(left)
        right_subarray = self.sortArray(right)

        return self.merge(left_subarray, right_subarray)

    
    def merge(self, left_subarray, right_subarray):
        l, r = 0, 0 
        res = []

        while l < len(left_subarray) and r < len(right_subarray):
            if left_subarray[l] < right_subarray[r]:
                res.append(left_subarray[l])
                l += 1
            else:
                res.append(right_subarray[r])
                r += 1
        
        if left_subarray:
            res.extend(left_subarray[l:])
        if right_subarray:
            res.extend(right_subarray[r:])
        
        return res





    
