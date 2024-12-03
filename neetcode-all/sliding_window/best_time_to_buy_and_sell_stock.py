class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0   
        max_p = 0

        for r in range(len(prices)):
            if prices[r] > prices[l]:
                current = prices[r] - prices[l]
                max_p = max(max_p, current)
            else:
                l = r
        return max_p
        
