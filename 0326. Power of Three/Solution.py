class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Or somehow use the log(n, 3) method
        
        if n <= 0:
            return False
        if n == 1:
            return True
        
        tmp = 3
        
        while tmp <= n:
            
            if tmp == n:
                return True
            tmp *= 3
        
        return False
