class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        s_list = []
        t_list = []
        
        for char in s:
            if char not in s_dict:
                s_dict[char] = len(s_dict.keys())
            s_list.append(s_dict[char])
        
            
        
        for char in t:
            if char not in t_dict:
                t_dict[char] = len(t_dict.keys())
            t_list.append(t_dict[char])
        
        return s_list == t_list
        
        
