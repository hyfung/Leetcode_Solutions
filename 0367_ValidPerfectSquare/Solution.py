class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        import math
        return math.sqrt(num) == int(math.sqrt(num))
        
