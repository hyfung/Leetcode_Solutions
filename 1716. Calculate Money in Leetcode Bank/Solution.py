class Solution:
    def totalMoney(self, n: int) -> int:
        full_week = n // 7
        excess_day = n % 7
        total = 0

        for i in range(0, full_week):
            total += 28 + (i)*7
        
        for i in range(1, excess_day+1):
            total += (full_week) + i
        
        return total
