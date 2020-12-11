class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1. We don't want negative numbers & 0s
        # 2. We sort the array for linear search
        nums = [x for x in sorted(nums) if x > 0]
        
        lowest = 0
        
        # If the array is []
        # Simply return 1
        if nums == []:
            return 1
        
        # If the array is [1]
        # Simply return 2
        if nums == [1]:
            return 2
        
        # If the array only has 1 element, it must be larger than 1
        # Simply return 1
        if len(nums) == 1:
            return min(1, nums[0])
        
        # Use a sliding window to compute
        # If the arithmetic difference is larger than 1, then there must be a gap between 2 numbers
        # And we store that number
        for i, num in enumerate(nums):
            if i == 0:
                continue
            if nums[i] - nums[i-1] > 1:
                # Found lowest
                lowest = nums[i] - 1
                break
        
        # Two cases, we either:
        # Didn't find any gap
        # The array consists of same elements
        if lowest == 0:
            if nums[0] != 1:
                return 1
            else:
                return nums[-1] + 1
                
        # Iterate through 1 to LOWEST_FOUND
        # If we don't see it in the array, it is the answer
        # If we saw that number, then we try the next one
        for i in range(1, lowest + 1):
            if i in nums:
                continue
            return i
