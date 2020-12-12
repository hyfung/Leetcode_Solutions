class Solution:
    def toLowerCase(self, str: str) -> str:
        # Use ASCII offset: Uppercase + 32 = Lowercase
        # a-z = 97-122
        # A-Z = 65-90
        new_str = ""
        for char in str:
            if ord(char) in range(65,90+1):
                # Perform conversion
                new_str += chr(ord(char) + 32)
            else:
                new_str += char
        
        return new_str
        
        # Otherwise we just call str.lower() in Python3
        
