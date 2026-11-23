class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Ok so for this one, while I have discovered an O(n^2) solution
        I will go for an O(n) Solution
        however the O(n) solution will be O(n) space as opposed to O(1)

        My approach for this would be to initialize a dictionary
        we start from the first element
        add it to the dictionary if not already there
        if it is increment the count
        """
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
        