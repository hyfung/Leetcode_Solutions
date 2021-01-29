class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            s = s.replace("0","x")
            s = s.replace("1", "0")
            s = s.replace("x", "1")
            return s
        
        sTmp = "0"
        for i in range(1, n):
            sTmp = sTmp + "1" + invert(sTmp)[::-1]
        
        return sTmp[k-1]
