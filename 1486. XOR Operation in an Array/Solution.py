class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        from functools import reduce
               
        return reduce(lambda x, y: x^y, [start+2*i for i in range(n)])
        
        
