import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        N = len(nums)
        
        arr = copy.copy(nums)

        for i in range(len(nums)):
            nums[i] = arr[(i+N-k) % N]
            
