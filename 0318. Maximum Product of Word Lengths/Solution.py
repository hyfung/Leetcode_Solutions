class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = []
        ret = 0
        
        for word in words:
            sets.append(set([ch for ch in word]))
        
        for i in range(len(sets)-1, -1, -1):
            for j in range(i-1,-1, -1):
                if i !=  j and set.isdisjoint(sets[i], sets[j]):
                    ret = max(ret,  len(words[i])*len(words[j]))
        
        return ret
        
