class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        N = len(nums)
        
        for i in range(N):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
        
        print(hashmap)
        
        for _,v in hashmap.items():
            if len(v) == 1:
                continue
                
            for i in range(len(v)-1):
                if abs(v[i] - v[i+1]) <= k:
                    return True
        
        return False
