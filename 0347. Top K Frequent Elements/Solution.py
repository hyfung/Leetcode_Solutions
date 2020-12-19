class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = dict()
        
        for num in nums:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1
        
        occur = sorted(list(occur.items()), key = lambda x: x[1], reverse=True)
        
        return [x[0] for x in occur[:k]]
        
        
