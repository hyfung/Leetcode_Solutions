class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        locations = []
        for i,v in enumerate(nums):
            if v == 1:
                locations.append(i)
        
        for i in range(len(locations) - 1):
            if (locations[i+1] - locations[i]) < (k + 1):
                return False
            
        return True
        
