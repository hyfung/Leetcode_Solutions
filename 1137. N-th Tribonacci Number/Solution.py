class Solution:
    # Look Up Table
    lut = dict()
    lut[0] = 0
    lut[1] = 1
    lut[2] = 1
    
    def tribonacci(self, n: int) -> int:
        
        # If we didn't see N, then cache it's result
        # If we seen N, then reuse the result
        
        if n not in Solution.lut:
            Solution.lut[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return Solution.lut[n]
        
