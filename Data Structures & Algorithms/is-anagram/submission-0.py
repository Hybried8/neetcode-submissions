class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        news = sorted(s)
        newt = sorted(t)

        if news == newt:
            return True
        
        return False
        
        