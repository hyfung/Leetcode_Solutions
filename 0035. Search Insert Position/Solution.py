class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            if target <= nums[0]:
                return 0
            if target > nums[-1]:
                return len(nums)
            
            
            for i in range(len(nums) - 1):
                if target < nums[i+1] and target > nums[i]:
                    return i+1
            return len(nums)
        
