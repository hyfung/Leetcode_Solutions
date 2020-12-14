class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        appear = dict()
        n = len(nums)
        res = []
        
        for i,v in enumerate(nums):
            if v not in appear:
                appear[v] = 1
            else:
                appear[v] += 1
            if appear[v] > n//3 and v not in res:
                res.append(v)               
        
        return sorted(res)
