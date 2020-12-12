class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = len(nums)//2
        
        ret_nums = []
        
        for i in range(length):
            ret_nums.append(nums[i])
            ret_nums.append(nums[i+length])
        
        return ret_nums
        
