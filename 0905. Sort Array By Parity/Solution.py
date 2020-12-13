class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if not x % 2] + [x for x in A if  x % 2]
        
