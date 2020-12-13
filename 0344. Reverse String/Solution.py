class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = len(s) // 2
        for i in range(count):
            tmp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = tmp
            
        
