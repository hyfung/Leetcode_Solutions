class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) <= 1:
            return True
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        if ord(word[0]) in range(65, 91) and word[1:] == word[1:].lower():
            return True
        
        return False
        
