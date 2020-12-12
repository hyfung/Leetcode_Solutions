class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # Optimized solution: binary search
        # Simple solution: list comprehension
        counter = 0
        for row in grid:
            counter += len([ele for ele in row if ele < 0])
        
        return counter
        
