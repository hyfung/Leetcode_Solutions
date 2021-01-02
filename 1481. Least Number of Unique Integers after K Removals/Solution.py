class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = dict()
        
        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        print(hashmap)
        
        arr = sorted(arr, key = lambda x: (hashmap[x], x), reverse=True)
        
        print(arr)
        
        for i in range(k):
            arr.pop()
            
        return len(set(arr))
