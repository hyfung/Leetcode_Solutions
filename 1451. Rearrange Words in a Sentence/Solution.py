class Solution:
    def arrangeWords(self, text: str) -> str:
        x = " ".join(sorted(text.split(' '), key=lambda x: len(x))).lower()
        
        x = x[0].upper() + x[1:]
        
        return x
        
        
