class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Check if we need to do padding
        # Because [0,0,1] is a fucking marginal case
        length = len(digits)
        
        if digits == [0]:
            return [1]
        
        if digits == [0,0]:
            return [0,1]
            
        sum = 0
        for digit in digits:
            sum = sum * 10 + digit
        sum += 1
        
        tmp_ret = [int(x) for x in str(sum)]
        if len(tmp_ret) < length:
            # Padding needed
            tmp_ret = [0] * (length-len(tmp_ret)) + tmp_ret
        return tmp_ret
