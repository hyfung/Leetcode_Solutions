class Solution:
    def reorderSpaces(self, text: str) -> str:
        if " " not in text:
            return text
        
        spaces = len([x for x in text if x == ' '])
        print(spaces)
        
        words = [x for x in text.strip(" ").split(" ") if x is not '']
        iWords = len(words)
        
        if iWords == 1:
            return words[0] + " " * spaces
        
        return (" " * ((spaces)//(iWords - 1))).join(words) + " " * (spaces % (iWords - 1))
        
