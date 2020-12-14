class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb = sorted(nums1 + nums2)
        len_comb = len(comb)
        
        if len_comb % 2 == 0:
            return (comb[len_comb//2] + comb[len_comb//2 -1]) / 2
        else:
            return comb[len_comb//2]
        
