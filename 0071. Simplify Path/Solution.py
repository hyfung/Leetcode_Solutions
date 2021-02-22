class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip('/')
        path = path.split('/')
        
        stack = []
        
        for token in path:
            if token == '':
                continue
            if token == '.':
                continue
            elif token == '..':
                try:
                    stack.pop()
                except:
                    pass
            else:
                stack.append(token)
        
        return '/'+'/'.join(stack)
        
