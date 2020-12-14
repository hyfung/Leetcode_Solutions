class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur = dict()
        for char in s:
            if char not in occur:
                occur[char] = 1
            else:
                occur[char] += 1

        for i,char in enumerate(s):
            if occur[char] == 1:
                return i
        return -1
            
