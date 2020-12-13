class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = [word[::-1] for word in s.split(' ')]
        return " ".join(new_s)
                
