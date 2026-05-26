class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        UMPIRE:
        We want to find 2 numbers in nums where adding them results in target
        input: array of integers, integer
        constraints: there is always 1 answer
        output: array of integers

        nums = [3,4,5,6] target = 9
                i     j
        
         target = 
             i      j
        """
        out = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    out.append(i)
                    out.append(j)


        return [out[0], out[1]]
            