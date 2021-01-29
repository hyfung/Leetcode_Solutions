class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        aStr = [str(x) for x in A]
        aBool = [False] * len(A)
        
        iTmp = 0
        for i,v in enumerate(A):
                iTmp = (iTmp << 1) + v
                if iTmp % 5 == 0:
                    aBool[i] = True
                
        return aBool
        
