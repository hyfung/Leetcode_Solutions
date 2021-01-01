class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = dict()
        count = 0
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        print(d)
        
        for key in d.keys():
            
            if 2 * key == k:
                while d[key] > 1:
                    count += 1
                    d[key] -= 2
            else:
                if (k-key) in d and key in d:
                    while d[k-key] > 0 and d[key] > 0:
                        d[k-key] -= 1
                        d[key] -= 1
                        count += 1
        
        return count
                    
        
