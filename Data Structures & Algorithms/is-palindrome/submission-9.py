class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        U
        This problem is checking if the contents of s would be the same forwards or backwards
        it is ignoring all spaces
        it does not care if uppercase or lower case

        MAtch:
        Clearly 2 pointers

        Plan:
        -First we turn all the contents of s to lowercase
        - We remove all the whitespaces
        - We remove everything that's not a letter or number
        - we initialize 2 pointers, left and right:
            - left goes to the right, right goes to the left
            - if at any point right != left return false
        - return true at the end
        """

        lowers = s.lower()
        lowers = "".join(char for char in lowers if char.isalnum())
        
        left = 0
        right = len(lowers) - 1


        if len(lowers) <= 1:
            return True

        if lowers[left] != lowers[right]:
            return False

        while (right > left):
            left += 1
            right -= 1

            if lowers[left] != lowers[right]:
                return False
    
        return True
        print(lowers)