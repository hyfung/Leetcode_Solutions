class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        result = 0
        
        if dividend < 0:
            dividend *= -1
            flag *= -1
        
        if divisor < 0:
            divisor *= -1
            flag *= -1
            
        while dividend >= divisor and dividend is not 0:
            dividend -= divisor
            result += 1
        
        return result * flag
        
