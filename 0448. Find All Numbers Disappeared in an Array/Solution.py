class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = dict()
        res = []
        for i in range(1,len(nums)+1):
            hashmap[i] = 0
        
        for num in nums:
            hashmap[num] += 1
        
        for k,v in hashmap.items():
            if v == 0:
                res.append(k)
                
        return res
        
