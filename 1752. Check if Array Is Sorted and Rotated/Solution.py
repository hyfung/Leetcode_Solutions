import copy

class Solution:
    def check(self, nums: List[int]) -> bool:
        new_nums = copy.copy(nums)
        new_nums.sort()
        new_nums = 2 * new_nums
        
        start = new_nums.index(nums[0])
        
        for start in range(len(new_nums)):
            if nums == new_nums[start:start+len(nums)]:
                return True
            
        return False
                
