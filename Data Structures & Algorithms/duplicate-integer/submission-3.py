class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = {}
        for i in nums:
            if i not in result:
                result[i] = 1
            else:
                return True
        return False