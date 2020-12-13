class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occurence = dict()
        for v in arr:
            if v not in occurence:
                occurence[v] = 1
            else:
                occurence[v] += 1
                
            if occurence[v] > len(arr)/4:
                return v
        
        
