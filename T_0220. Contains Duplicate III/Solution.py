"""
Requires time complexity optimization
e.g. Using hashmap of i,j
"""

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        hashmap = dict()
        N = len(nums)
        for i in range(N - 1):
            for j in range(i + 1, N):
                if abs(i-j) <= k:
                    if abs(nums[i] - nums[j]) <= t:
                        return True
        return False
        
