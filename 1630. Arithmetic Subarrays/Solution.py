class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lBool = [True] * len(l)
        
        for i in range(len(l)):
            lTmp = nums[l[i]:r[i]+1]
            lTmp.sort()
            iDiff = lTmp[0] - lTmp[1]
            for j in range(len(lTmp) - 1):
                if lTmp[j] - lTmp[j+1] != iDiff:
                    lBool[i] = False
        
        return lBool
        
