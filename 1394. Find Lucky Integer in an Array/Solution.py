class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = dict()
        res = -1
        
        for k,v in enumerate(arr):
            if v not in hashmap:
                hashmap[v] = 1
            else:
                hashmap[v] += 1
        
        for k,v in hashmap.items():
            if k == v:
                res = max(res, k)
                
        return res
        
        
