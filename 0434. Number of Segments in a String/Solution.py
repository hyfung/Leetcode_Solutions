class Solution:
    def countSegments(self, s: str) -> int:
        # If its empty
        if s == "":
            return 0
        
        # If it is all whitespaces:
        if len(s.strip(' ')) == 0:
            return 0
        
        # Remove all leading and trailing spaces
        s = s.strip(' ')
        
        return len([x for x in s.split(' ') if x is not ''])
