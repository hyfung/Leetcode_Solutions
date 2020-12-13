class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        occurence = dict()
        
        for i,v in enumerate(nums):
            if v not in occurence:
                occurence[v] = 1
            else:
                occurence[v] += 1
        
        miss = None
        for i in range(1, len(nums)+1):
            if i not in occurence:
                miss = i
            
        # dup = None
        # for k,v in nums.items():
        #     if v == 2:
        #         dup = k
        dup = [k for k,v in occurence.items() if v == 2][0]
        
        return [dup, miss]
        
