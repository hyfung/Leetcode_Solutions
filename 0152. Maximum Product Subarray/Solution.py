class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        from functools import reduce
        
        max_product = -2147483648
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j >= i:
                    max_product = max(max_product, reduce(lambda x,y: x*y, nums[i:j+1]))
            
        return max_product
                
