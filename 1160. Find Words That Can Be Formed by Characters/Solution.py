class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_d = dict()
        ret = 0
        
        # Build a signature map for chars
        for ch in chars:
            if ch in char_d:
                char_d[ch] += 1
            else:
                char_d[ch] = 1
        
        # Profile each word in words
        for word in words:
            valid = True
            
            tmp_d = dict()
            for ch in word:
                if ch in tmp_d:
                    tmp_d[ch] += 1
                else:
                    tmp_d[ch] = 1
                        
            # Check if all characters in word occurs in char_d
            for k,v in tmp_d.items():
                try:
                    if v > char_d[k]:
                        valid = False
                except:
                    valid = False
            
            if valid:
                ret += len(word)
        
        return ret
    
