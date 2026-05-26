class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        res = []

        for i in nums:
            if i not in out:
                out[i] = 0
            if i in out:
                out[i] += 1
        
        while k > 0:
            max_key = max(out, key=out.get)
            res.append(max_key)
            out.pop(max_key)
            k -= 1
    
        return res
        