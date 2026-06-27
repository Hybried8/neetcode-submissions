class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize result array (filled with 0s to match the length)
        res = [0] * len(temperatures)
        
        # start from the first element
        for i in range(len(temperatures)):
            # initialize a count variable at 1
            counter = 1
            # initialize a pointer (starts at the next element after i)
            j = i + 1
            
            # move to the next until we get to the end of the array
            while j < len(temperatures):
                # if the next element after it is greater
                if temperatures[j] > temperatures[i]:
                    # add counter to array
                    res[i] = counter
                    # initialize counter back to 1 (handled implicitly by the break/outer loop)
                    break
                else:
                    # if it is not greater, increment counter
                    counter += 1
                
                # move to the next
                j += 1
            
            # if we get to the end of array without finding a warmer day:
            # counter = 1 and add 0 to the array (res[i] remains 0 as initialized)
            
        return res