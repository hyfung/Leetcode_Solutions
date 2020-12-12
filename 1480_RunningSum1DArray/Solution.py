class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret_nums = [0] * len(nums)
        
        for i, v in enumerate(nums):
            ret_nums[i] = sum(nums[:i+1])
        
        return ret_nums
