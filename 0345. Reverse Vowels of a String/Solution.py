class Solution:
    def reverseVowels(self, s: str) -> str:
        # Make a stack which stores all vowels
        vowels = []
        
        # Tokenize the string for easier modification since string is not mutable
        s_token = [char for char in s]
        
        # Iterate through the string to find all vowels
        # Push all vowels onto the stack and mark the original string
        for i,v in enumerate(s):
            if v in 'aeiouAEIOU':
                vowels.append(v)
                s_token[i] = '中'

        # Filling tha gaps
        for i, v in enumerate(s_token):
            if v == '中':
                s_token[i] = vowels.pop()
        
        return "".join(s_token)
        
        print(s_token)
        print(vowels)
                
        
