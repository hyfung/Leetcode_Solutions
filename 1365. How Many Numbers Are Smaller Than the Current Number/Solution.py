class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list = [0] * len(nums)
        
        for i,v in enumerate(nums):
            new_list[i] = len([x for x in nums if x < v])
            
        return new_list
