class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap_ransom = dict()
        hashmap_mag = dict()
        
        for char in ransomNote:
            if char in hashmap_ransom:
                hashmap_ransom[char] += 1
            else:
                hashmap_ransom[char] = 1
        
        for char in magazine:
            if char in hashmap_mag:
                hashmap_mag[char] += 1
            else:
                hashmap_mag[char] = 1
                
        for k,v in hashmap_ransom.items():
            try:
                if not hashmap_ransom[k] <= hashmap_mag[k]:
                    return False
            except:
                return False
        
        return True
        
        
        
