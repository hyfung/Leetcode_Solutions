class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        counter = 1
        max_cnt = 1
        
        if nums == []:
            return 0
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                counter += 1
                max_cnt = max(max_cnt, counter)
                continue
            else:
                max_cnt = max(max_cnt, counter)
                counter = 1
        
        return max_cnt
        
