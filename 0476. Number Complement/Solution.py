class Solution:
    def findComplement(self, num: int) -> int:
        s = "{0:b}".format(num)
        s = s.replace('1', '#')
        s = s.replace('0', '1')
        s = s.replace('#', '0')
        
        return eval('0b' + s)
        
