class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        result = 0
        for i in range(0,length,2):
            result += min(nums[i], nums[i+1])
            
        return result
        
