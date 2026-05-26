class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The idea here is that we find which words are anagrams and then group them
        My thought process is that:
        for each word we come across:
        - we make a result list:
            if word not in any of existing lists, make a new list and add word to it
            if word in any of existing lists, add word to it
        - return the list of lists.
        """
        result = []

        """
        def findAna(self, str1: str, str2: str):
            sortstr1 = sorted(str1)
            sortstr2 = sorted(str2)

            if sortstr1 == sortstr2:
                return True
            
            return False
        """
        
        for word in strs:
            found = False
            for group in result:
                if sorted(group[0]) == sorted(word):
                    group.append(word)
                    found = True
                    break
            if not found:
                result.append([word])
        
        return result



                

        