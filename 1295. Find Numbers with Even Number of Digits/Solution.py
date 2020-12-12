class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # Approach 1: itoa
        counter = 0
        for i, v in enumerate(nums):
            if len(str(v)) % 2 == 0:
                counter += 1
        return counter
        
        # Optimization/Refactor
        # Use list comprehension to filter odd numbers out
        # return len() of the list
        
        # Approach 2: while n//10 increment counter
        
