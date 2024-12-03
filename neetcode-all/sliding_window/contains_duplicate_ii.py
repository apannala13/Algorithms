class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i, n in enumerate(nums):
            if n in hashmap and hashmap[n] != i and abs(hashmap[n] - i) <= k:
                return True
            hashmap[n] = i
        return False
        
