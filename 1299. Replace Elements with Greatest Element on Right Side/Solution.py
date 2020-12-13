class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = []
        for i in range(len(arr) - 1):
            ret.append(max(arr[i+1:]))
        ret.append(-1)
        return ret
        
