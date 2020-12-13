class Solution:
    def thousandSeparator(self, n: int) -> str:
        ret_str = ""
        while n > 1000:
            ret_str = '.' + str(n)[-3:] + ret_str
            n //= 1000
        return str(n) + ret_str
        
        
