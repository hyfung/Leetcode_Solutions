class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        myarr = [x for x in list(range(1, 2002)) if x not in arr] 
        
        return myarr[k-1]
        
