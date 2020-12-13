class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = []
        t_stack = []
        
        for i in S:
            if i != '#':
                s_stack.append(i)
            else:
                if s_stack != []:
                    s_stack.pop()
        
        for i in T:
            if i != '#':
                t_stack.append(i)
            else:
                if t_stack != []:
                    t_stack.pop()
        
        return s_stack == t_stack
