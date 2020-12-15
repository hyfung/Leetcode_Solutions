class Solution:
    def reverseBits(self, n: int) -> int:
        str_n = "{0:b}".format(n)
        str_n = "0" * (32 - len(str_n)) + str_n
        str_n = str_n[::-1]
        return eval("0b" + str_n)
        
