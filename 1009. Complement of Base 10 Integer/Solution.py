class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        return eval("0b" + "".join(["0" if char is "1" else "1" for char in "{0:b}".format(N)]))
        
        
