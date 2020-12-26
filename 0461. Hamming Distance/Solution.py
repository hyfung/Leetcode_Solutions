class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return len([char for char in "{0:b}".format(x ^ y) if char == '1'])
        
