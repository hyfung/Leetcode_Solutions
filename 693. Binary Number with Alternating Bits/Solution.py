class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if '00' in "{0:b}".format(n) or '11' in "{0:b}".format(n):
            return False
        return True
        
