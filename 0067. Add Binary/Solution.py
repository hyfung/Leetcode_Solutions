class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # First we do padding
        pad = abs(len(a) - len(b))
        
        if len(a) > len(b):
            b = "0" * pad + b
        
        if len(b) > len(a):
            a = "0" * pad + a
        
        # Then we implement a simple binary adder
        res_str = ""
        carry = 0
        for i in range(len(a)-1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry
            
            carry = 0
            if sum > 1:
                sum %= 2
                carry = 1
            
            res_str = str(sum) + res_str
        
        # If carry bit is set, we add it to the beginning of our output string
        if carry:
            res_str = '1' + res_str
            
        return res_str
