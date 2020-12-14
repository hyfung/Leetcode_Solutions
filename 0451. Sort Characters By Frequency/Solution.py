class Solution:
    def frequencySort(self, s: str) -> str:
        # First we construct a hashmap
        occur = dict()
        
        for char in s:
            if char not in occur:
                occur[char] = 1
            else:
                occur[char] += 1
        
        return "".join([x[0] * x[1] for x in sorted(list(occur.items()), key=lambda x: x[1], reverse=True)])
        
