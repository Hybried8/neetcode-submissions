class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search
        we start from the middle
        if greater than slice the left
        if less than slice the right
        keep going until empty or you find
        then return undex
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return -1

        
        