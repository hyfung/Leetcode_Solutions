class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # Solution without converting to string
        
        # Optimization: Use fixed size array instead of using list to increase memory efficiency
        # Since the length of integer is fixed
        
        # 0-9 is always palindrome
        if x in range(0,10):
            return True
        
        # Negative numbers are always not palindrome
        if x < 0:
            return False
        
        # Now we only check positive numbers
        stack = []
        tmp = x
        
        # First breakdown the integer to single digits and push it onto a stack
        while tmp > 0:
            stack.append(tmp%10)
            tmp //= 10
        
        # Matching head and tails
        # Only need to enumerate half of the array, e.g.
        # Length 6: check 0,1,2
        # Length 7: check 0,1,2
        for i, v in range(len(stack)//2):
            if stack[i] != stack[-i-1]:
                return False
        return True
        
        
