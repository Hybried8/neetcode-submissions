class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        We have a constraint of constant space..
        
        Honestly only solution I can think up is we start
        left at index 0, right at left + 1
        so from there we start at 0 and 1
        if they equal target we return them
        if not then we move right 
        then move right 
        until the end
        if we get to the end, we move left to left + 1
        right at the new left + 1
        then we do the same 
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1