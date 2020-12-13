class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        myset = 'abcdefghijklmnopqrstuvwxyz'
        s_dict = dict()
        t_dict = dict()
        
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
                
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        for char in myset:
            if s_dict.get(char) != t_dict.get(char):
                return char
        
