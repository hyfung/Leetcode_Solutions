class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        ls = [ch for ch in S]
        
        chs = []
        
        for i,v in enumerate(ls):
            if v.isalpha():
                chs.append(ls[i])
                ls[i] = None
        
        for i,v in enumerate(ls):
            if ls[i] is None:
                ls[i] = chs.pop()
        
        
        return "".join(ls)
                
        
        
