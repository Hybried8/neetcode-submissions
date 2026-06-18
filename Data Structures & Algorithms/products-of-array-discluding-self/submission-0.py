class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            # Create a fresh copy of the list each time
            current_elements = nums.copy() 
            # Remove the element at the current index
            current_elements.pop(i) 
            
            # Multiply the remaining elements
            product = 1
            for a in current_elements:
                product *= a
            
            result.append(product)
            
        return result