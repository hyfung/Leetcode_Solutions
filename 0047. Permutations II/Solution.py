class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        
        permus = permutations(nums)
        
        occur = set()
        res = []
        
        for permu in permus:
            if str(permu) in occur:
                continue
            else:
                occur.add(str(permu))
                res.append(permu)
        
        return res
        
