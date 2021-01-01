class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        if len(A) > len(B):
                return False
        return A in B * 2 and A is not "" and B is not ""
        
