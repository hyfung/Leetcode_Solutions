class Solution:
    def maximum69Number (self, num: int) -> int:
        # Nothing to do if no 6
        if '6' not in str(num):
            return num
        
        
        
        # Solution: replace the first 6 with 9
        
        location = str(num).index('6')
        
        amount = 10**(len(str(num)) - location -1) * 3
        
        return num + amount
