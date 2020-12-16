class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1 or len(nums) == 2:
            return []
        
        res = []
        sol_set = set()
        two_sums = dict()
        N = len(nums)
        
        for i in range(N):
            for j in range(i+1, N):
                two_sums[(i,j)] = nums[i] + nums[j]
                
        for i in range(N):
            for k,v in two_sums.items():
                if i in k:
                    continue
                if -nums[i] == v:
                    sol = sorted([i,k[0],k[1]])
                    sol = sorted([ nums[sol[0]], nums[sol[1]], nums[sol[2]] ])
                    sol_set.add((sol[0], sol[1], sol[2]))
        
        return list(sol_set)
        
        
