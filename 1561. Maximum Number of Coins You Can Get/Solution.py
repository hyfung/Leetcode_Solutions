class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        iRet = 0
        piles.sort()
        
        while piles:
            iRet += piles[-2]
            piles.pop()
            piles.pop()
            piles.pop(0)
            
        return iRet
        
