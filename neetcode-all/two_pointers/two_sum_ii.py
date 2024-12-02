class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force, worst - o(n^2)
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return 

        #hashmap - o(n) time, o(n) space 
        hashmap = {}

        for i, n in enumerate(numbers):
            diff = target - n 
            if diff in hashmap:
                return [hashmap[diff] + 1, i + 1]
            hashmap[n] = i 
        return 


        #most optimized: two pointers - o(n) time, o(1) space 
        l, r = 0, len(numbers) - 1
        for i in range(len(numbers)):
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return 
