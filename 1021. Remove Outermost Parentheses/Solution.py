class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        sRes = ""
        
        sOpen = False
        counter = 0
        
        for ch in S:
            if ch == '(':
                if not sOpen:
                    sOpen = True
                    continue
                else:
                    counter += 1
                    sRes += '('
                
            if ch == ')':
                if sOpen and counter == 0:
                    sOpen = False
                    continue
                else:
                    sRes += ')'
                    counter -= 1
                
                
        return sRes
                
