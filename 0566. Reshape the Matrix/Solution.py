class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        
        if len(nums)*len(nums[0]) != r * c:
            return nums
        
        res = np.array(nums).reshape(r,c)
        
        return res
        
