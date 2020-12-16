class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()
        
        two_sum = dict()
        
        for i in range(N):
            for j in range(i, N):
                two_sum[i, j] = nums[i] + nums[j]
        
        triplets = []
        for i in range(N):
            triplets += [sorted([k[0],k[1],i]) for k,v in two_sum.items() if v == -nums[i] and i != k[0] and i != k[1] and k[0] != k[1]]
        
        
        for t in triplets:
            tmp = [nums[t[0]],nums[t[1]],nums[t[2]]]
            if tmp not in res:
                res.append(tmp)
        
        return res
        
