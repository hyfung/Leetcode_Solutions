import copy
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        scores = sorted(copy.copy(nums), reverse=True)
        mapping = dict()
        
        for i,v in enumerate(scores):
            if i == 0:
                mapping[v] = "Gold Medal"
            elif i == 1:
                mapping[v] = "Silver Medal"
            elif i == 2:
                mapping[v] = "Bronze Medal"
            else:
                mapping[v] = str(i+1)
        
        return [mapping[x] for x in nums]
