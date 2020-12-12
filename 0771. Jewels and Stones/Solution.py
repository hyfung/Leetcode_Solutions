class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = 0
        for j in J:
            for s in S:
                if j == s:
                    counter += 1
        
        return counter
