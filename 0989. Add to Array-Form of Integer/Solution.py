class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return ([int(x) for x in str(int("".join([str(x) for x in A])) + K)])

        
