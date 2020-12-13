class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr3 = sorted([x for x in arr1 if x not in arr2])
        
        arr1 = [x for x in arr1 if x in arr2]
        
        occurence = dict()
        
        for i in arr1:
            if i not in occurence:
                occurence[i] = 1
            else:
                occurence[i] += 1
        
        out_ls = []
        
        for i in arr2:
            out_ls += [i] * occurence[i]
        
        out_ls += arr3
        
        return out_ls
        
