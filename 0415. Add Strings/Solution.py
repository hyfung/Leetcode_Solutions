class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # Use adder approach
        # First we pad the shorter string
        diff = abs(len(num1) - len(num2))
        if len(num1) > len(num2):
            # pad num2
            num2 = "0" * diff + num2
            
        if len(num2) > len(num1):
            # pad num1
            num1 = "0" * diff + num1
        
        # Start from the end
        # Prepare a new string
        
        res = ""
        
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            tmp = int(num1[i]) + int(num2[i]) + carry
            carry = 0
            if tmp >= 10:
                carry = 1
                tmp %= 10
            
            res = str(tmp) + res
        if carry:
            res = '1' + res
            
        return res

        
        
