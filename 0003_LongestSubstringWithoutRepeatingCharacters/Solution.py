class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret_val = 0
        if len(s) == 1:
            return 1
        
        for i, v in enumerate(s):
            longest_str = ""
            substr = s[i:]
            
            for char in substr:
                if char not in longest_str:
                    longest_str += char
                else:
                    break
            ret_val = max(ret_val, len(longest_str))        
            print(longest_str)
                
        return ret_val
    
