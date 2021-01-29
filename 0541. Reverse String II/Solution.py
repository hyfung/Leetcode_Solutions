class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sRes = ""
        
        for i in range(0, int(len(s)/k) + 1):
            if i % 2 == 0:
                # Reverse
                sRes += s[i*k:(i+1)*k][::-1]
            else:
                sRes += s[i*k:(i+1)*k]
        
        return sRes
        
