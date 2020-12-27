class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                v = stones.pop(-2)
                stones[-1] -= v
            stones.sort()
        
        return stones[0] if stones else 0
        
