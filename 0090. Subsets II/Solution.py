class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        import itertools
        N = len(nums)
        res = []
        
        for i in range(0, N+1):
            res += [tuple(sorted(x)) for x in itertools.combinations(nums, i)]
        
        return list(set(res))
        
        
