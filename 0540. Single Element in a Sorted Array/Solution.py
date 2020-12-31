class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        hashmap = dict()
        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
                
        return [k for k,v in hashmap.items() if v == 1][0]
