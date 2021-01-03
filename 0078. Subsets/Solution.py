class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        import itertools
        N = len(nums)
        res = []
        
        for i in range(0, N+1):
            res += [list(x) for x in itertools.combinations(nums, i)]
        
        return res
        
