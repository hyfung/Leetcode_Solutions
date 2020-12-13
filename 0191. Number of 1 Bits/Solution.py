class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([i for i in "{0:b}".format(n) if i == "1"])
        
        
