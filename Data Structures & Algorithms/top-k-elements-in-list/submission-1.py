class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Here, we want to find the top k most frequent elements.
        What will happen is that we find the most frequent element in the list.
        When we do we reduce k by 1, add the element to result and
         remove all occurrences of said element from nums
        """
        result = []

        def findtopfreq(num: List[int]):
            freq = Counter(num)
            return max(freq, key=freq.get)

        while k > 0 and nums:
            top = findtopfreq(nums)
            result.append(top)

            nums = [x for x in nums if x != top]

            k -= 1

        return result
        
        
        