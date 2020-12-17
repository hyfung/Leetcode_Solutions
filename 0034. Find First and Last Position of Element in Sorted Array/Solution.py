class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Further optimization: Use Binary Search
        
        first_occur, last_occur = -1, -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                first_occur = i if first_occur == -1 else first_occur
                last_occur = max(i, last_occur)
        
        return [first_occur, last_occur]
        
