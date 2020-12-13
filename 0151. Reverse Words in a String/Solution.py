class Solution:
    def reverseWords(self, s: str) -> str:
        # Remove leading and trailing whitespaces
        s = s.strip(" ")
        
        # Split the words
        s = [x for x in s.split(' ') if x != '']
        
        # Reverse the list
        s = s[::-1]
        
        # Join the words
        return " ".join(s)
        
