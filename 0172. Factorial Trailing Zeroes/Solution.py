class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        def factorial(n):
            if n == 0:
                return 0
            if n == 1:
               return n
            else:
               return n*factorial(n-1)
        
        s = str(factorial(n))
        return len(s) - len(s.rstrip('0'))
        
