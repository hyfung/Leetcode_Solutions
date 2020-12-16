class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = dict()
        
        
        for i,word in enumerate(list1):
            if word in list2:
                hashmap[word] = i if word not in hashmap else hashmap[word] + i
            
        for i,word in enumerate(list2):
            if word in list1:
                hashmap[word] = i if word not in hashmap else hashmap[word] + i
        
        lowest_index = min(hashmap.values())
        
        return [k for k,v in hashmap.items() if v == lowest_index]
        
        
