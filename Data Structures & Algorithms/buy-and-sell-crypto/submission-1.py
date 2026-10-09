class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        current_prof = 0

        if len(prices) == 1:
            return 0
        
        for right in range(1,len(prices)):
            while prices[left] > prices[right]:
                left += 1
            current_prof = max(current_prof, prices[right] - prices[left] )
        
        return current_prof

        