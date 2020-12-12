class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'x'
        if n == 2:
            return 'xy'
        if n % 2 == 0:
            return 'x' * (n-1) + 'y'
        else:
            return 'x' * n
        
