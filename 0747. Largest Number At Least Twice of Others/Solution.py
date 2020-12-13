class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        new_nums = sorted(nums)
        if new_nums[-1] >= 2 * new_nums [-2]:
            return nums.index(new_nums[-1])
        else:
            return -1
        
