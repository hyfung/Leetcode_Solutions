class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        
        for char in s:
            if char in '({[':
                stack.append(char)
                
            if char == ')':
                if stack == []:
                    return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
                
            if char == '}':
                if stack == []:
                    return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
                
            if char == ']':
                if stack == []:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        if len(stack) > 0:
            return False
        
        return True
        
