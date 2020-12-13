class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # Check similarity
        # - All similar & no dup -> False
        # - All similar & has dup -> True
        # - 1 different -> False
        # - 2 different -> Continue
        # - 3 or more different -> False
        
        # Early return as there's no fit
        if len(A) != len(B):
            return False
        
        diff = 0
        diff_index = []
        a_sort = sorted(A)
        b_sort = sorted(B)
        
        for i in range(len(A)):
            # Early return as there's no fit
            if a_sort[i] != b_sort[i]:
                return False
            
            if A[i] != B[i]:
                diff += 1
                diff_index.append(i)
        
        
        
        if diff == 0:
            tmp_d = dict()
            for i,v in enumerate(A):
                if v not in tmp_d:
                    tmp_d[v] = 1
                else:
                    tmp_d[v] += 1
            if len([x for x in tmp_d.values() if x > 1]) > 0:
                return True
            else:
                return False
            
        if diff == 1:
            return False
        if diff > 2:
            return False
        
        return True
        
