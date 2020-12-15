class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def isPalin(s):
            for i in range(len(s)//2):
                if s[i] != s[-i-1]:
                    return False
            return True
        
        N = len(a)
        for i in range(N):
            a1, a2 = a[:i], a[i:]
            b1, b2 = b[:i], b[i:]
            # b1, b2 = b[:i][::-1], b[i:][::-1]
            
            
            if isPalin(a1+b2) or isPalin(b1+a2):
                return True
            
            # Combination 1
            # print(a1+b2)
            
            # Combination 2
            # print(b1+a2)
        
        return False
        
